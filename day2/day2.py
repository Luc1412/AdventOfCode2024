def part1(data) -> int:
    res = 0
    for data_points in data:
        # Lists are not increasing or decreasing
        if check_increase_decrease(data_points):
            continue
        if not check_diff(data_points, [1, 2, 3]):
            continue
        res += 1
    return res


def part2(data) -> int:
    res = 0
    for data_points in data:
        # Create variants of datapaoints by removing one element
        data_points_variants = [
            data_points[:i] + data_points[i + 1 :] for i in range(len(data_points))
        ]
        valid = False
        for data_points_variant in data_points_variants:
            # Lists are not increasing or decreasing
            if not check_increase_decrease(data_points_variant):
                continue
            if not check_diff(data_points_variant, [1, 2, 3]):
                continue
            valid = True
            break
        if valid:
            res += 1
    return res


def check_increase_decrease(dps) -> bool:
    return sorted(dps) == dps or sorted(dps, reverse=True) == dps


def check_diff(dps, allowed_diffs) -> bool:
    curr = None
    for dp in dps:
        if curr is None:
            curr = dp
            continue
        diff = abs(curr - dp)
        if diff not in allowed_diffs:
            return False
        curr = dp
    return True


if __name__ == "__main__":
    with open("input") as f:
        data = f.read().splitlines()

    data_points = [[int(dp) for dp in line.split(" ")] for line in data]

    print(f"Res1: {part1(data_points)}")
    print(f"Res2: {part2(data_points)}")
