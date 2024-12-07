def part1(data) -> int:
    res = 0
    operators = ["+", "*"]

    for line in data:
        test_value, numbers_str = map(str.strip, line.split(": "))
        test_value = int(test_value)
        numbers = tuple(map(int, numbers_str.split()))

        for i in range(len(operators) ** (len(numbers) - 1)):
            operator = [
                operators[(i // (len(operators) ** j)) % len(operators)]
                for j in range(len(numbers) - 1)
            ]
            eval_str = (
                " ".join(f"{numbers[k]} {operator[k]}" for k in range(len(numbers) - 1))
                + f" {numbers[-1]}"
            )

            if test_value == calculate(eval_str):
                res += test_value
                break

    return res


def part2(data) -> int:
    res = 0
    operators = ["+", "*", "||"]

    for line in data:
        test_value, numbers_str = map(str.strip, line.split(": "))
        test_value = int(test_value)
        numbers = tuple(map(int, numbers_str.split()))

        for i in range(len(operators) ** (len(numbers) - 1)):
            operator = [
                operators[(i // (len(operators) ** j)) % len(operators)]
                for j in range(len(numbers) - 1)
            ]
            eval_str = (
                " ".join(f"{numbers[k]} {operator[k]}" for k in range(len(numbers) - 1))
                + f" {numbers[-1]}"
            )

            if test_value == calculate(eval_str):
                res += test_value
                break

    return res


def calculate(eval_str: str) -> int:
    tokens = eval_str.split()
    result = int(tokens[0])
    for j in range(1, len(tokens), 2):
        op, num = tokens[j], int(tokens[j + 1])
        if op == "+":
            result += num
        elif op == "*":
            result *= num
        elif op == "||":
            result = int(f"{result}{num}")
    return result


if __name__ == "__main__":
    with open("input") as f:
        data = f.read().splitlines()

    print(f"Res1: {part1(data)}")
    print(f"Res2: {part2(data)}")
