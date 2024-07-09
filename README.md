## Installation
```
# Install poetry
curl -sSL https://install.python-poetry.org | python3 -

# Clone this repo
git clone git@github.com:renStori/poormans-test.git
cd poormans-test

# Install dependencies
poetry install --no-root

# Execute
poetry run python main.py --email poormans-email@yopmail.com # By default --password is Holamundo1

# Erase CURP
poetry run python erase_curp.py --email stori.cosmos22@yopmail.com # By default --password is Holamundo1
```

## Documentation

[Read the docs.](https://github.com/renStori/poormans-test/blob/main/main.py)
