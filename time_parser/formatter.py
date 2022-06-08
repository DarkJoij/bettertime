import typing

from . import parser


def format_parts(
    datearray: typing.List[typing.Tuple[str, str]],
    language: typing.Literal['ru', 'en']
) -> str:
    aliases = {}
    
    for date_package, name in parser.Dates.ALL:
        if language == 'en':
            aliases[name] = date_package[0]
        else:
            aliases[name] = date_package[4]

    result = str()

    for date, name in datearray:
        result += f'{date}{aliases[name]} '

    return result
