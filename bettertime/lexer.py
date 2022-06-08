import re
import typing

from . import exceptions
from . import regex


class Lexer:
    tokens = [] 
    position = 0

    def __init__(self, expression: str) -> None:
        self.code = expression

    def next_token(self) -> bool:
        if self.position >= len(self.code):
            return False

        for token_type in regex.TYPES:
            type_regex = regex.TYPES[token_type]
            type_regex = re.compile(type_regex)
            matched = type_regex.match(self.code, self.position)

            if matched.group():
                string = matched.group()
                group = token_type
                token = regex.Token(string, group)

                self.tokens.append(token)
                self.position += len(matched.group())
                return True

        raise exceptions.InvalidCharacterError(
            f'Met invalid character at position: {self.position}.'
        )

    def lex(self) -> typing.List[regex.Token]:
        while self.next_token():  # Not ideal, but usefull method.
            pass

        for token in self.tokens:
            if token.group == 'empty':
                self.tokens.remove(token)

        return self.tokens
