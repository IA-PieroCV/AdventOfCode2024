from math import log10


def main(n_blinks: int = 1):
    with open("input.txt", "r") as file:
        eval_lines = file.read()

    stones = list(map(lambda stone: int(stone), eval_lines.split()))

    for bkidx in range(n_blinks):
        print("BLINK NUM", bkidx, "OF", n_blinks)
        stones = blink(stones)
        print(len(stones))

    print(len(stones))

def blink(stones: list[int | None]) -> list[int | None]:
    new_stones = []
    for stone in stones:
        stone_res = blink_stone(stone)
        new_stones.extend(stone_res)

    return new_stones


def blink_stone(stone: int) -> list[int]:
    stone_res = []

    if stone:
        digits = int(log10(stone) + 1)
        even_digits = digits % 2 == 0

    if not stone:
        stone_res.append(1)
    elif even_digits:
        stone_res.append(int(str(stone)[: digits // 2]))
        stone_res.append(int(str(stone)[digits // 2 :]))
    else:
        stone_res.append(stone * 2024)

    return stone_res


if __name__ == "__main__":
    main(n_blinks = 25)
    main(n_blinks = 75)
