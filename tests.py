from time_parser import to_seconds

not_parsed_time = '1год 13месяцев 120дней 40часов 70минут 140секунд'
parsed_time = to_seconds(not_parsed_time)
print(parsed_time)
