'''
Time Parser Module.
~~~~~~~~~~~~~~~~~~~

Module converting string date 
expressions to seconds [int].

:copyright: (c) 2022 Dallas
:license: MIT, see `MIT License` for more details.

'''

__title__ = 'time_parser'
__author__ = 'Dallas'
__license__ = 'MIT'
__version__ = '0.0.0'

from .lexer import Lexer
from .parser import Parser


def new_line() -> str:
    return '\n'


def to_seconds(expression: str) -> int:
    '''
    Function converting `str` expressions written on
    human date format to seconds.
    
    Examples:
     `to_seconds('2hours')` -> 7200.\n
     `to_seconds('3h 45m 20s')` -> 13520.
    
    Support:
     Languages:
      RU, EN, ru, en.
     Date parts:
      'year': (
         'y', 'year', 'ys', 'years',
         'г', 'лет', 'год', 'года'
        ),
        'month': (
         'mon', 'month', 'ms', 'months',
         'мес', 'месяцев'
        ),
        'day': (
         'd', 'day', 'ds', 'days',
         'д', 'дней', 'дня', 'день'
        ),
        'hours': (
         'h', 'hour', 'hs', 'hours',
         'ч', 'час', 'часов', 'часа'
        ),
        'minute': (
         'm', 'min', 'mins', 'minute', 'minutes',
         'м', 'мин', 'минут', 'минуты', 'минута'
        ),
        'second': (
         's', 'seconds', 'seconds',
         'с', 'сек', 'секунды', 'секунда', 'секунд'
        )

    :param expression: [str] Text-expression with integer numbers
    and string date-parts.

    :return: [int] Seconds got from summing expression tokens.

    :raises:
     InvalidCharacterError: When lexer cannot match symbol with reserved.
     ExpresionError: When in expression found fewer than 2 tokens.
     TokenOrderError: WHen token going not in order like `number, string`...
    '''

    tokens = Lexer(expression).lex()
    seconds = Parser(tokens).parse_to_seconds()

    return seconds
