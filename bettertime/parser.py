import typing
from dataclasses import dataclass

from . import exceptions
from . import formatter
from . import regex


# Not very comfortable, but I'm lazy to replace 
@dataclass
class Dates:
    YEAR = (
        'y', 'year', 'ys', 'years',
        'г', 'год', 'лет', 'года'
    )
    MONTH = (
        'mon', 'month', 'ms', 'months',
        'мес', 'месяц', 'месяцев', 'месяца'
    )
    DAY = (
        'd', 'day', 'ds', 'days',
        'д', 'день', 'дней', 'дня',
    )
    HOUR = (
        'h', 'hour', 'hs', 'hours',
        'ч', 'час', 'часов', 'часа'
    )
    MINUTE = (
        'm', 'min', 'minute', 'minutes',
        'м', 'мин', 'минут', 'минуты', 'минута'
    )
    SECOND = (
        's', 'sec', 'seconds', 'seconds',
        'с', 'сек', 'секунды', 'секунда', 'секунд'
    )

    ALL = (
        (YEAR, 'year'), (MONTH, 'month'), (DAY, 'day'), 
        (HOUR, 'hour'), (MINUTE, 'minute'), (SECOND, 'second')
    )


to_seconds = {
    'year': 31104000,
    'month': 2592000,
    'day': 86400,
    'hour': 3600,
    'minute': 60,
    'second': 1
}

class Parser:
    position = 0

    def __init__(self, tokens: typing.List[regex.Token]) -> None:
        if len(tokens) < 2:
            raise exceptions.ExpressionError(
                f'In expression found fewer than 2 parts. Make it bigger.'
            )
        self.tokens = tokens
    
    @staticmethod
    def _parse_to_number(this_token: regex.Token, 
                         other_token: regex.Token) -> typing.Union[int, bool]:
        for date_package, name in Dates.ALL:
            if other_token.string.lower() in date_package:
                try:
                    return int(this_token.string) * to_seconds[name]
                except ValueError:
                    return False
        return False


    def parse_to_seconds(self) -> int:
        expression_value = 0

        while self.position < len(self.tokens):
            this_token = self.tokens[self.position]
            token_index = self.tokens.index(this_token)
            next_token = self.tokens[token_index + 1]

            parsed = False
                
            if (this_token.group, next_token.group) == ('number', 'string'):
                parsed = self._parse_to_number(this_token, next_token)
            
            if not parsed:
                raise exceptions.TokenError(
                    f'Cannot parse token with string: \'{this_token.string}\'.'
                )

            expression_value += parsed
            self.position += 2

        return expression_value

    @staticmethod
    def parse_to_string(seconds: int,
                        language: typing.Literal['ru', 'en'] = 'ru') -> str:
        datearray = []

        for date in to_seconds:
            part, seconds = divmod(seconds, to_seconds[date])
            if part > 0:
                datearray.append((str(part), date))

        return formatter.format_parts(datearray, language)
