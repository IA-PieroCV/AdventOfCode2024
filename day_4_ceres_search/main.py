import re


def get_start_positions(full_text: str, character: str) -> list[tuple[int, int]] | None:
    rows = len(full_text.split("\n"))
    x_finds = list(re.finditer(character, full_text.replace("\n", "")))
    if x_finds:
        return list(
            map(lambda x_find: (x_find.start() // rows, x_find.start() % rows), x_finds)
        )


def get_valid_xmas(start_position: tuple[int, int], full_text: str) -> int:
    full_text = full_text.split("\n")
    total_rows, total_columns = len(full_text), len(full_text[0])
    row, column = start_position
    have_up_limit = row < 3
    have_down_limit = row > total_rows - 4
    have_left_limit = column < 3
    have_right_limit = column > total_columns - 4

    total = 0

    if not have_up_limit:
        coinc = (
            full_text[row][column]
            + full_text[row - 1][column]
            + full_text[row - 2][column]
            + full_text[row - 3][column]
        )
        if coinc == "XMAS":
            total += 1

    if not have_down_limit:
        coinc = (
            full_text[row][column]
            + full_text[row + 1][column]
            + full_text[row + 2][column]
            + full_text[row + 3][column]
        )
        if coinc == "XMAS":
            total += 1

    if not have_left_limit:
        coinc = (
            full_text[row][column]
            + full_text[row][column - 1]
            + full_text[row][column - 2]
            + full_text[row][column - 3]
        )
        if coinc == "XMAS":
            total += 1

    if not have_right_limit:
        coinc = (
            full_text[row][column]
            + full_text[row][column + 1]
            + full_text[row][column + 2]
            + full_text[row][column + 3]
        )
        if coinc == "XMAS":
            total += 1

    if not (have_up_limit or have_left_limit):
        coinc = (
            full_text[row][column]
            + full_text[row - 1][column - 1]
            + full_text[row - 2][column - 2]
            + full_text[row - 3][column - 3]
        )
        if coinc == "XMAS":
            total += 1

    if not (have_up_limit or have_right_limit):
        coinc = (
            full_text[row][column]
            + full_text[row - 1][column + 1]
            + full_text[row - 2][column + 2]
            + full_text[row - 3][column + 3]
        )
        if coinc == "XMAS":
            total += 1

    if not (have_down_limit or have_left_limit):
        coinc = (
            full_text[row][column]
            + full_text[row + 1][column - 1]
            + full_text[row + 2][column - 2]
            + full_text[row + 3][column - 3]
        )
        if coinc == "XMAS":
            total += 1

    if not (have_down_limit or have_right_limit):
        coinc = (
            full_text[row][column]
            + full_text[row + 1][column + 1]
            + full_text[row + 2][column + 2]
            + full_text[row + 3][column + 3]
        )
        if coinc == "XMAS":
            total += 1

    return total


def get_valid_x_mas(start_position: tuple[int, int], full_text: str) -> int:
    full_text = full_text.split("\n")
    total_rows, total_columns = len(full_text), len(full_text[0])
    row, column = start_position
    have_up_limit = row < 1
    have_down_limit = row > total_rows - 2
    have_left_limit = column < 1
    have_right_limit = column > total_columns - 2

    if not (have_up_limit or have_down_limit or have_left_limit or have_right_limit):
        coinc1 = (
            full_text[row - 1][column - 1] == "M"
            and full_text[row - 1][column + 1] == "M"
            and full_text[row + 1][column + 1] == "S"
            and full_text[row + 1][column - 1] == "S"
        )

        coinc2 = (
            full_text[row - 1][column - 1] == "S"
            and full_text[row - 1][column + 1] == "M"
            and full_text[row + 1][column + 1] == "M"
            and full_text[row + 1][column - 1] == "S"
        )

        coinc3 = (
            full_text[row - 1][column - 1] == "S"
            and full_text[row - 1][column + 1] == "S"
            and full_text[row + 1][column + 1] == "M"
            and full_text[row + 1][column - 1] == "M"
        )

        coinc4 = (
            full_text[row - 1][column - 1] == "M"
            and full_text[row - 1][column + 1] == "S"
            and full_text[row + 1][column + 1] == "S"
            and full_text[row + 1][column - 1] == "M"
        )

        return int(coinc1 or coinc2 or coinc3 or coinc4)
    return 0


def main():
    with open("input.txt", "r") as file:
        lines = file.read()

    start_positions: list[tuple[int, int]] | None = get_start_positions(lines, "X")

    total_xmas = 0
    if start_positions is not None:
        for start_position in start_positions:
            total_xmas += get_valid_xmas(start_position, lines)

    print(total_xmas)

    start_positions: list[tuple[int, int]] | None = get_start_positions(lines, "A")

    total_x_mas = 0
    if start_positions is not None:
        for start_position in start_positions:
            total_x_mas += get_valid_x_mas(start_position, lines)

    print(total_x_mas)


if __name__ == "__main__":
    main()
