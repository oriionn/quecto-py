# quecto-py
Quecto-py is a simple and official wrapper of Quecto, an open-source and self-hostable solution for link shortening.

## Installation
```bash
pip install quecto
```

## Usage
### Shorten a link
```python
from quecto import Quecto

client = Quecto("https://s.oriondev.fr")
r = client.shortUrl("https://example.com", "password") # password is optional
print(r) # https://s.oriondev.fr/s/189d28e9b9ae6
```
### Unshorten a link
```python
from quecto import Quecto

client = Quecto("https://s.oriondev.fr")
r = client.unshortUrl("https://s.oriondev.fr/s/189d28e9b9ae6", "password") # password is optional
print(r) # https://example.com
```
### Check if the domain is a valid Quecto instance
```python
from quecto import Quecto

client = Quecto("https://s.oriondev.fr")
r = client.isValidInstance()
print(r) # True
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

![Contributors](https://contrib.rocks/image?repo=oriionn/quecto-py)

## License
[GPL3](https://github.com/oriionn/quecto-py/blob/main/LICENSE)