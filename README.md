# Secret Santa

## Requirements

- `pipenv`
- `python-black`
- `python-flake8`

## Usage

First, copy the `config-sample.yaml` and `santas-sample.json` files, to update
it with your own data.

```bash
cp config-sample.yaml config.yaml
cp santas-sample.json santas.json
```

Edit the `config.yaml` and `santas.json` files to fit your needs, according to
the templates. The `mail` field in `config.yaml` is the email address used to
send mails to each santas.

Then run the program in its environment.

```bash
pipenv shell
pip install -r requirements.txt
make
```
