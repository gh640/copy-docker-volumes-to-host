# Copy Docker volumes to host

This is a sample Python script to copy all Docker (named) volumes to host.

## Prerequisites

- Python 3
- Docker for Mac

## Usage

Check how things work with `--dry-run` option.

```bash
python3 copy_docker_volumes_to_host.py --dry-run
```

Output:

```text
Total volumes: 5
volume_a:
volume_b:
volume_c:
volume_d:
volume_e:
```

If the behavior looks fine, run the script without `--dry-run`. Volumes will be copied into the `volumes/` directory.

```bash
python3 copy_docker_volumes_to_host.py
```

Output:

```text
Total volumes: 5
volume_a:
return code: 0
volume_b:
return code: 0
volume_c:
return code: 0
volume_d:
return code: 0
volume_e:
return code: 0
```
