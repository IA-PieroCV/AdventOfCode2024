import re


def get_unique_frequencies(full_text: str):
    chars = list(set(list(full_text.replace(".", "").replace("\n", ""))))
    return chars


def get_frequency_locations(frequency: str, full_text: str):
    cols = len(full_text.split("\n")[0])
    anthenas = list(re.finditer(f"{frequency}", full_text.replace("\n", "")))
    anthenas = list(map(lambda x: (x.start() // cols, x.start() % cols), anthenas))
    return anthenas


def get_frequency_pairs(freq_locations: tuple[str]):
    pairs = []
    for index, location in enumerate(freq_locations):
        _ = [
            pairs.append((location, pair_freq))
            for pair_freq in freq_locations[index + 1 :]
        ]
    return pairs


def get_antinodes(pair_frequency: tuple[tuple[str]], full_text: str, single: bool):
    ans = []

    lines = full_text.split("\n")
    rows, cols = len(lines), len(lines[0])
    p1, p2 = pair_frequency
    dif_x = p2[0] - p1[0]
    dif_y = p2[1] - p1[1]

    out_of_map = out_a1 = out_a2 = False
    mult = 1

    while not out_of_map:
        a1 = (p1[0] - (dif_x * mult), p1[1] - (dif_y * mult))
        a2 = (p2[0] + (dif_x * mult), p2[1] + (dif_y * mult))

        if 0 <= a1[0] < rows and 0 <= a1[1] < cols:
            ans.append(a1)
        else:
            out_a1 = True

        if 0 <= a2[0] < rows and 0 <= a2[1] < cols:
            ans.append(a2)
        else:
            out_a2 = True

        if single or (out_a1 and out_a2):
            out_of_map = True

        mult += 1

    return ans


def main(part: str, single: bool):
    with open("input.txt", "r") as file:
        eval_lines = file.read()
    full_antinodes = set()
    unique_frequencies = get_unique_frequencies(eval_lines)

    for frequency in unique_frequencies:
        all_frequencies_location = get_frequency_locations(frequency, eval_lines)
        frequency_pairs = get_frequency_pairs(all_frequencies_location)

        for pair_frequency in frequency_pairs:
            antinodes = get_antinodes(pair_frequency, eval_lines, single)
            _ = [full_antinodes.add(an) for an in antinodes]

        if frequency_pairs and not single:
            _ = [full_antinodes.add(an) for an in all_frequencies_location]

    print(f"PART {part}:", len(sorted(list(full_antinodes))))


if __name__ == "__main__":
    main(part="1", single=True)
    main(part="2", single=False)
