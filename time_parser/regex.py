from dataclasses import dataclass


TYPES = {
    'string': r'[a-zA-Zа-яА-Я]*',
    'number': r'[0-9]*',
    'empty': r'[ \n\t\r]*'
}


@dataclass
class Token:
    string: str
    group: str
