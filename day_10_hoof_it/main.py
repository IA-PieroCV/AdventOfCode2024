import re


def main():
    with open("input.txt", "r") as file:
        eval_lines = file.read()
    topographic_lines = eval_lines.split("\n")
    rows, cols = len(topographic_lines), len(topographic_lines[0])
    start_pos = [
        (sp.start() // cols, sp.start() % cols)
        for sp in re.finditer("0", eval_lines.replace("\n", ""))
    ]

    paths = 0
    for sp in start_pos:
        total_heads = set(find_best_path(sp, topographic_lines, rows, cols))
        paths += len(total_heads)
    print("PART 1:", paths)

    paths = 0
    for sp in start_pos:
        total_heads = find_best_path(sp, topographic_lines, rows, cols)
        paths += len(total_heads)
    print("PART 2:", paths)


def find_best_path(current_position, topographic_lines, rows, cols):
    current_value = topographic_lines[current_position[0]][current_position[1]]
    if int(current_value) == 9:
        return [current_position]
    else:
        found_path_1, found_path_2, found_path_3, found_path_4 = [], [], [], []
        if (
            current_position[0] != 0
            and int(topographic_lines[current_position[0] - 1][current_position[1]])
            == int(current_value) + 1
        ):
            found_path_1 = find_best_path(
                (current_position[0] - 1, current_position[1]),
                topographic_lines,
                rows,
                cols,
            )

        if (
            current_position[0] != rows - 1
            and int(topographic_lines[current_position[0] + 1][current_position[1]])
            == int(current_value) + 1
        ):
            found_path_2 = find_best_path(
                (current_position[0] + 1, current_position[1]),
                topographic_lines,
                rows,
                cols,
            )

        if (
            current_position[1] != 0
            and int(topographic_lines[current_position[0]][current_position[1] - 1])
            == int(current_value) + 1
        ):
            found_path_3 = find_best_path(
                (current_position[0], current_position[1] - 1),
                topographic_lines,
                rows,
                cols,
            )

        if (
            current_position[1] != cols - 1
            and int(topographic_lines[current_position[0]][current_position[1] + 1])
            == int(current_value) + 1
        ):
            found_path_4 = find_best_path(
                (current_position[0], current_position[1] + 1),
                topographic_lines,
                rows,
                cols,
            )

        total_found = found_path_1 + found_path_2 + found_path_3 + found_path_4
        return total_found


if __name__ == "__main__":
    main()
