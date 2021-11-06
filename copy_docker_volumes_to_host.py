#!/usr/bin/env python3
"""Copy all Docker volumes to host. """

import argparse
import subprocess
from pathlib import Path

PARENT = Path(__file__).resolve().parent / 'volumes'
IMAGE = 'alpine:latest'


def main() -> None:
    args = get_args()
    dry_run = args.dry_run

    volume_names = list_volume_names()
    print(f'Total volumes: {len(volume_names)}')

    for volume_name in volume_names:
        print(f'{volume_name}:')
        if dry_run:
            continue

        process = copy_volume_to_host(PARENT, volume_name)
        print_command_result(process)


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument('--dry-run', action='store_true')
    return parser.parse_args()


def list_volume_names() -> list[str]:
    process = execute(['docker', 'volume', 'ls', '-q'])
    return process.stdout.decode().splitlines()


def copy_volume_to_host(parent: Path, volume_name: str) -> subprocess.CompletedProcess:
    if not volume_name:
        raise ValueError(f'volume_name must not be empty.')

    command = [
        'docker',
        'run',
        '--rm',
        '-v',
        f'{volume_name}:/from/{volume_name}',
        '-v',
        f'{str(parent)}:/to',
        IMAGE,
        'sh',
        '-c',
        # コピー先のディレクトリが存在しない場合のみ実行する
        f'test -d /to/{volume_name} || cp -r /from/{volume_name} /to/',
    ]
    return execute(command)


def execute(command: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(command, capture_output=True, check=True)


def print_command_result(process: subprocess.CompletedProcess) -> None:
    print(f'return code: {process.returncode}')


if __name__ == '__main__':
    main()
