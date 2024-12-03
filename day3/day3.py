import re

MUL_REGEX = re.compile(
    r"(?P<op>mul|do|don\'t)\((?:(?P<mul1>\d{1,3}),(?P<mul2>\d{1,3}))?\)"
)


def part1(data) -> int:
    # Find all mul regexes and multiple all numbers
    res = 0
    for line in data:
        mul = MUL_REGEX.findall(line)
        for operator, a, b in mul:
            if operator == "mul":
                res += int(a) * int(b)

    return res


def part2(data) -> int:
    res = 0
    enabled = True
    for line in data:
        mul = MUL_REGEX.findall(line)
        for operator, a, b in mul:
            if operator == "mul" and enabled:
                res += int(a) * int(b)
            elif operator == "do":
                enabled = True
            elif operator == "don't":
                enabled = False
    return res


if __name__ == "__main__":
    with open("input") as f:
        data = f.read().splitlines()

    print(f"Res1: {part1(data)}")
    print(f"Res2: {part2(data)}")
