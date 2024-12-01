from collections import Counter

with open("input.txt", "r") as file:
    lines = file.readlines()

digits = map(lambda x: x.split(), lines)
sorted_digits = list(map(sorted, zip(*digits)))
distances = map(lambda x: abs(int(x[0]) - int(x[1])), zip(*sorted_digits))
print(sum(distances))

id_counter = Counter(sorted_digits[1])
print(sum(map(lambda x: int(x) * id_counter.get(x, 0), sorted_digits[0])))
