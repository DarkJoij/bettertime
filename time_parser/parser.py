import typing

from . import regex
from . import exceptions


# `NamedTuple` and everything simple to it go fuck itself.
class DateParser:
    date_aliases = {
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
    }
    
    to_number = {
        'year': 31104000,
        'month': 2592000,
        'day': 86400,
        'hours': 3600,
        'minute': 60,
        'second': 1
    }

    @classmethod
    def parse_to_number(cls, this: regex.Token, other: regex.Token) -> typing.Union[int, bool]:
        for date_part in cls.date_aliases:
            if other.string.lower() in cls.date_aliases[date_part]:
                other = date_part
                return int(this.string) * cls.to_number[other]
        return False


class Parser:
    position = 0

    def __init__(self, tokens: typing.List[regex.Token]) -> None:
        if len(tokens) < 2:
            raise exceptions.ExpresionError(
                f'In expression found fewer than 2 parts. Make it bigger.'
            )
        self.tokens = tokens

    def parse_to_seconds(self) -> int:  # Just some fun.
        expression_value = 0

        while self.position < len(self.tokens):
            token = self.tokens[self.position]
            token_index = self.tokens.index(token)
            next_token = self.tokens[token_index + 1]
                
            if (token.group, next_token.group) == ('number', 'string'):
                parsed = DateParser.parse_to_number(token, next_token)
                if not parsed:
                    raise exceptions.TokenOrderError(
                        f'Two tokens ({token}, {next_token}) going ordered with similar types.'
                    )

                expression_value += parsed
                self.position += 2

        return expression_value
