# Time Parser
**Time Parser** - is a Python library, converting string date expressions to seconds [int].

# Installition
#### PyPI:
```py
$ [py -m] pip install time_parser
```
#### GitHub:
```py
$ git clone https://github.com/DarkJoij/time_parser
```

# Examples
#### Converting from string expressions to seconds:
```py
from time_parser import to_seconds

print(to_seconds('5hours 30minutes'))
```
```py
19800
```

#### Converting from seconds to string expressions:
```py
from time_parser import to_string

print(to_string(793800, language='en'))
```
```py
9d 4h 30m
```

* Function `to_seconds` take parameter `expression: str`.
* Function `to_string` take 2 parameters: `seconds: int`, `language: 'ru' | 'en' = 'ru'`.

To see all dates aliases check file [time_parser/parser.py](https://github.com/DarkJoij/time_parser/blob/main/time_parser/parser.py). 

Sweet using and building your lovely dsbots)
