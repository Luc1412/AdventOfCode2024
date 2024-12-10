def part1(data) -> int:
    res = 0

    for trail_head in find_trail_heads(data):
        peaks = list()
        walk_trail(data, trail_head, 0, peaks)
        res += len(set(peaks))
    return res


def walk_trail(
    data, loc: tuple[int, int], height: int, visited: list[tuple[int, int]]
) -> None:
    x, y = loc
    # If we've reached 9 we got a complete trail
    if data[y][x] == 9:
        visited.append((x, y))
        return

    # Walk in all directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_within_bounds(nx, ny, data) and data[ny][nx] == height + 1:
            walk_trail(data, (nx, ny), height + 1, visited)


def is_within_bounds(x, y, data) -> bool:
    return 0 <= x < len(data[0]) and 0 <= y < len(data)


def find_trail_heads(data) -> list[tuple[int, int]]:
    return [
        (x, y) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] == 0
    ]


def part2(data) -> int:
    peaks = list()
    for trail_head in find_trail_heads(data):
        walk_trail(data, trail_head, 0, peaks)
    return len(peaks)


if __name__ == "__main__":
    with open("input") as f:
        data = [
            list(map(lambda l: int(l) if l.isdigit() else -1, l))
            for l in f.read().splitlines()
        ]
    print(f"Res1: {part1(data)}")
    print(f"Res2: {part2(data)}")
