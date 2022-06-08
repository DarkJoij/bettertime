from time_parser import to_seconds, to_string

parsed_time = to_seconds('8дней 12часов 45минут 35секунд')
print(parsed_time)

already_not_parsed = to_string(34245)
print(already_not_parsed)
