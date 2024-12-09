import numpy as np


def main():
    with open("input.txt", "r") as file:
        eval_lines = file.read()

    memory = eval_lines[0::2]
    spaces = eval_lines[1::2]
    spaces = spaces + "0" if len(memory) > len(spaces) else spaces

    raw_disk = []
    for index, (mem, space) in enumerate(zip(memory, spaces)):
        raw_disk.extend([index] * int(mem))
        raw_disk.extend(["."] * int(space))

    raw_disk = np.array(raw_disk)

    ordered_disk = raw_disk.copy()

    dots_idxs = np.equal(ordered_disk, ".")
    num_quant = len(ordered_disk[~dots_idxs])
    subpart_nums = ordered_disk[num_quant:]
    final_nums = subpart_nums[subpart_nums != "."][::-1]
    mask = dots_idxs & (np.arange(len(ordered_disk)) < num_quant)
    ordered_disk[mask] = final_nums
    ordered_disk[num_quant:] = "."

    final_sum = [idx * int(char) for idx, char in enumerate(ordered_disk[:num_quant])]
    print("PART 1:", sum(final_sum))

    sec_ordered_disk = raw_disk.copy()
    max_num = sec_ordered_disk[sec_ordered_disk != "."].astype(np.int64).max()

    for id in range(max_num, -1, -1):
        print("FINDING VALUE FOR:", id, end="\r")
        id_idxs = np.where(sec_ordered_disk == str(id))
        idi1 = min(id_idxs[0])
        idi2 = max(id_idxs[0]) + 1
        dots_mask = sec_ordered_disk == "."
        shifted = ~(np.hstack([np.array("0"), sec_ordered_disk[:-1]]) == ".")
        check_space_idxs = np.where(dots_mask & shifted)[0]
        found_space = False
        for dot_idx in check_space_idxs:
            di1, di2 = dot_idx, dot_idx + (idi2 - idi1)
            found_space = np.all(sec_ordered_disk[di1:di2] == ".")
            if found_space or dot_idx > idi1:
                break
        if found_space and idi1 > dot_idx:
            sec_ordered_disk[di1:di2] = sec_ordered_disk[idi1:idi2]
            sec_ordered_disk[idi1:idi2] = "."

    final_sum = [
        idx * int(char) for idx, char in enumerate(sec_ordered_disk) if char != "."
    ]
    print(" " * 30, end="\r")
    print("PART 2:", sum(final_sum))


if __name__ == "__main__":
    main()
