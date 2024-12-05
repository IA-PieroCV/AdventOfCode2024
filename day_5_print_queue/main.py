with open("input.txt", "r") as file:
    parts = file.read().split("\n\n")

rules = parts[0].split("\n")
sequences = parts[1].split("\n")

rules = list(map(lambda rule: (rule.split("|")), rules))

middles = 0
non_passing_lines = []

for sample_sequence in sequences:
    for sample_rule in rules:
        if sample_rule[0] in sample_sequence and sample_rule[1] in sample_sequence:
            if sample_sequence.index(sample_rule[0]) >= sample_sequence.index(
                sample_rule[1]
            ):
                non_passing_lines.append(sample_sequence)
                break
    else:
        nums = sample_sequence.split(",")
        middles += int(nums[len(nums) // 2])

print("PART 1:", middles)

non_passing_lines = list(map(lambda npl: npl.split(","), non_passing_lines))
middles = 0

for npl in non_passing_lines:
    relevant_rules = list(filter(lambda rule: rule[0] in npl and rule[1] in npl, rules))
    ordered_line = []
    while len(ordered_line) < len(npl):
        for num in npl:
            if num in ordered_line:
                continue
            for rule in relevant_rules:
                if rule[0] in ordered_line or rule[1] in ordered_line:
                    continue
                if num == rule[1]:
                    break
            else:
                ordered_line.append(num)
                break
    middles += int(ordered_line[len(ordered_line) // 2])

print("PART 2:", middles)
