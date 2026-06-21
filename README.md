# urli

A small helper to parse and display URLs — masks passwords in connection strings.

## Usage

```python
from urli.urli import remove_password

url = "mysql+aiomysql://user1:secret2@127.0.0.1/db_name"
print(remove_password(url))
# mysql+aiomysql://user1:****@127.0.0.1/db_name
```

## Demo

```bash
uv run python -m scripts.demo
```
