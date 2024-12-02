from itertools import combinations, compress

with open("input.txt", "r") as file:
    lines = file.readlines()

digit_list = list(map(lambda x: list(map(lambda y: int(y), x.split())), lines))
pairs = list(map(lambda line: list(zip(line, line[1:])), digit_list))
difference_result = list(
    map(lambda list_pairs: list(map(lambda x: abs(x[0] - x[1]), list_pairs)), pairs)
)
difference_list = list(
    map(
        lambda differences: all(map(lambda diff: 1 <= diff <= 3, differences)),
        difference_result,
    )
)
safe_lists = list(
    map(
        lambda x: (x[0] == sorted(x[0]) or x[0] == sorted(x[0], reverse=True)) and x[1],
        zip(digit_list, difference_list),
    )
)

print("RESULT 1:", sum(safe_lists))

rest_digits = list(compress(digit_list, map(lambda x: not x, safe_lists)))
rest_combinations = list(
    map(lambda digits: list(combinations(digits, len(digits) - 1)), rest_digits)
)
pairs_rest = list(
    map(
        lambda combination: list(
            map(lambda line: list(zip(line, line[1:])), combination)
        ),
        rest_combinations,
    )
)
difference_result_rest = list(
    map(
        lambda combination: list(
            map(
                lambda list_pairs: list(map(lambda x: abs(x[0] - x[1]), list_pairs)),
                combination,
            )
        ),
        pairs_rest,
    )
)
difference_list_rest = list(
    map(
        lambda combination: list(
            map(
                lambda differences: all(map(lambda diff: 1 <= diff <= 3, differences)),
                combination,
            )
        ),
        difference_result_rest,
    )
)
safe_lists_rest = list(
    map(
        lambda combination_zip: any(
            map(
                lambda x: (
                    list(x[0]) == sorted(x[0])
                    or list(x[0]) == sorted(x[0], reverse=True)
                )
                and x[1],
                zip(combination_zip[0], combination_zip[1]),
            )
        ),
        zip(rest_combinations, difference_list_rest),
    )
)
print("RESULT 2:", sum(safe_lists) + sum(safe_lists_rest))
