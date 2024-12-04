import numpy as np


def part1(data) -> int:
    res = 0

    def count(in_: str) -> int:
        return in_.count("XMAS") + in_.count("SAMX")

    # Horizontal rows
    horizontal_rows = ["".join(row) for row in data]
    for row in horizontal_rows:
        res += count(row)

    # Vertical rows
    vertical_rows = ["".join(row) for row in data.T]
    for row in vertical_rows:
        res += count(row)

    # Both diagonals
    diagonal_rows = [
        "".join(data.diagonal(i)) for i in range(-data.shape[0] + 1, data.shape[1])
    ] + [
        "".join(np.fliplr(data).diagonal(i))
        for i in range(-data.shape[0] + 1, data.shape[1])
    ]
    for row in diagonal_rows:
        res += count(row)

    return res


def part2(data) -> int:
    res = 0

    solutions = ("MAS", "SAM")
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            word1 = data[i - 1][j - 1] + data[i][j] + data[i + 1][j + 1]
            word2 = data[i - 1][j + 1] + data[i][j] + data[i + 1][j - 1]
            if word1 in solutions and word2 in solutions:
                res += 1
    return res


if __name__ == "__main__":
    with open("input") as f:
        data = f.read().splitlines()

    # Load data
    data = np.array([list(line) for line in data])

    print(f"Res1: {part1(data)}")
    print(f"Res2: {part2(data)}")
