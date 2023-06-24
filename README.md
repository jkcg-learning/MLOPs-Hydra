# MLOPs-Hydra

## Development

Install in dev mode

```
pip install -e .
pip install -r requirements.txt

```

```
sai_train --help
```

examples

- `sai_train data.num_workers=16`
- `sai_train data.num_workers=16 trainer.deterministic=True +trainer.fast_dev_run=True`

### Docker

```
docker build -f Dockerfile -t cifar-timm:latest .
docker run -it cifar-timm
sai_train

```