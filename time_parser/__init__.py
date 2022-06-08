'''
Better Time Module.
~~~~~~~~~~~~~~~~~~~

Library converting string
date expressions to seconds [int].

:copyright: (c) 2022 Dallas
:license: MIT, see `MIT License` for more details.
'''

__title__ = 'bettertime'
__author__ = 'Dallas'
__license__ = 'MIT'
__version__ = '1.0.0'

from typing import Literal

from .lexer import Lexer
from .parser import Parser


def to_seconds(expression: str) -> int:
    '''
    Function converting `str` expressions written on
    human date expressions to seconds. Letters case unsensetive.
    
    Examples:
       `to_seconds('2hours')` -> `7200`\n
       `to_seconds('3h 45m 20s')` -> `13520`

    :param expression: [str] Text-expression with integer numbers
    and string date-parts.

    :return: [int] Seconds got from summing expressions tokens.

    :raises:
       InvalidCharacterError: When lexer cannot match symbol with reserved.
       ExpresionError: When in expression found fewer than 2 tokens.
       TokenError: When parser cannot parse `token.string` in any case...
    '''
    tokens = Lexer(expression).lex()
    seconds = Parser(tokens).parse_to_seconds()
    return seconds


def to_string(seconds: int, language: Literal['ru', 'en'] = 'ru') -> str:
    '''
    Function converting `int` numbers to human 
    date string expressions. Default language is Russian.
    
    Examples:
       `to_string(737135)` -> `'8д 12ч 45м 35с'`\n
       `to_string(885300, language='en')` -> `'10d 5h 55m'`
     
    :param seconds: [int] Duration of date in seconds.
    :param language: [Literal['ru', 'en'] = 'ru'] Language 
    that will be used for naming date parts.

    :return: [str] String expression got from parsing seconds.
    '''
    string = Parser.parse_to_string(seconds, language)
    return string
