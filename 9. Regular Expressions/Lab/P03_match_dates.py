# Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy". Use capturing groups in your
# regular expression.
import re


text = input()
regex = r"\b(?P<day>\d{2})(?P<separator>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
matches = re.finditer(regex, text)

for match in matches:
    day = match.group("day")
    month = match.group("month")
    year = match.group("year")

    print(f"Day: {day}, Month: {month}, Year: {year}")