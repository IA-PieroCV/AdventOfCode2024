import re

with open("input.txt", "r") as file:
    lines = file.read()
    lines = lines.replace("\n", "")
regex_results = re.findall("mul\((\d{1,3}),(\d{1,3})\)", lines)
products = map(lambda x: int(x[0]) * int(x[1]), regex_results)
print(sum(products))

regex_to_remove = list(re.finditer("don't\(\)(.*?)do\(\)", lines))

for finding in regex_to_remove[::-1]:
    lines = lines[: finding.start()] + lines[finding.end() :]

regex_to_remove = re.finditer("don't\(\)", lines)
lines = lines[: next(regex_to_remove).start()]

regex_results = re.findall("mul\((\d{1,3}),(\d{1,3})\)", lines)
products = map(lambda x: int(x[0]) * int(x[1]), regex_results)
print(sum(products))
