with open("input.txt", "r") as file:
    eval_lines = file.read().split("\n")

equal_result = 0
for index, operation_line in enumerate(eval_lines):
    print("Evaluating", index + 1, "of", len(eval_lines), end="\r")
    numbers = operation_line.split(":")[-1].strip().split()
    expected_result = int(operation_line.split(":")[0].strip())
    op_quant = 2 ** (len(numbers) - 1)
    operations = [
        f"{bin(i)}".replace("0b", "").zfill(len(numbers) - 1) for i in range(op_quant)
    ]
    for operation in operations:
        number = int(numbers[0])
        for next_number, operator in zip(numbers[1:], operation):
            number = (
                number + int(next_number)
                if operator == "0"
                else number * int(next_number)
            )
        if number == expected_result:
            equal_result += expected_result
            break
print("PART 1:", equal_result)


def convert_to_base_3(number):
    final_num = ""
    while number != 0:
        final_num = str(number % 3) + final_num
        number //= 3
    return final_num


equal_result = 0
for index, operation_line in enumerate(eval_lines):
    print("Evaluating", index + 1, "of", len(eval_lines), end="\r")
    numbers = operation_line.split(":")[-1].strip().split()
    expected_result = int(operation_line.split(":")[0].strip())
    op_quant = 3 ** (len(numbers) - 1)
    operations = [convert_to_base_3(i).zfill(len(numbers) - 1) for i in range(op_quant)]
    for operation in operations:
        number = int(numbers[0])
        for next_number, operator in zip(numbers[1:], operation):
            number = (
                number + int(next_number)
                if operator == "0"
                else number * int(next_number)
                if operator == "1"
                else int(str(number) + next_number)
            )
        if number == expected_result:
            equal_result += expected_result
            break
print("PART 2:", equal_result)
