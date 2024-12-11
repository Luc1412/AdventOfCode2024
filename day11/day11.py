def part1(data) -> int:

    stones = data.copy()

    for _ in range(6):
        i = 0
        while i < len(data):
            stone = stones[i]
            # If stone is 0, we need to replace it with 1
            if stone == 0:
                stones[i] = 1
            # If stone has even number of digits, we need to split it in half. E.g. 1234 -> 12, 34
            elif len(str(stone)) % 2 == 0:
                half_len = len(str(stone)) // 2
                stones[i] = int(str(stone)[:half_len])
                stones.insert(i + 1, int(str(stone)[half_len:]))
                i += 1
            # Otherwise stone is multiplied by 2024
            else:
                stones[i] = stone * 2024
            i += 1

    return len(stones)


def part2(data) -> int:
    stones: dict[int, int] = {s: 1 for s in data}

    for _ in range(75):
        curr_stones = {}
        for stone, count in stones.items():
            # If stone is 0, we need to replace it with 1
            if stone == 0:
                curr_stones[1] = curr_stones.get(1, 0) + count
            # If stone has even number of digits, we need to split it in half. E.g. 1234 -> 12, 34
            elif len(str(stone)) % 2 == 0:
                half_len = len(str(stone)) // 2
                num1, num2 = int(str(stone)[:half_len]), int(str(stone)[half_len:])
                curr_stones[num1] = curr_stones.get(num1, 0) + count
                curr_stones[num2] = curr_stones.get(num2, 0) + count
            # Otherwise stone is multiplied by 2024
            else:
                new_stone = stone * 2024
                curr_stones[new_stone] = curr_stones.get(new_stone, 0) + count
        stones = curr_stones

    return sum(stones.values())


if __name__ == "__main__":
    with open("input") as f:
        data = list(map(int, f.readline().split(" ")))
    print(f"Res1: {part1(data)}")
    print(f"Res2: {part2(data)}")
