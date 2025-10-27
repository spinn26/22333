# analytics

## setup

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## install dlt and init pipeline

```sh
pip install "dlt[postgres]"
dlt init google_analytics postgres
```