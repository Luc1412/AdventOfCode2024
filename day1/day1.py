def part1(left_ids, right_ids) -> int:
    left_ids.sort()
    right_ids.sort()

    print(left_ids)
    print(right_ids)

    res = 0
    for i in range(len(left_ids)):
        right_nbr = right_ids[i]
        left_nbr = left_ids[i]
        ## Check distance
        dist = abs(int(right_nbr) - int(left_nbr))
        res += dist

    return res


def part2(left_ids, right_ids):

    res = 0
    for id_ in left_ids:
        count = right_ids.count(id_)
        res += count * int(id_)

    return res


if __name__ == "__main__":
    with open("day1_input") as f:
        data = f.read().splitlines()

    left_ids = list()
    right_ids = list()

    for line in data:
        left_nbr, right_nbr = line.split("   ")
        left_ids.append(left_nbr)
        right_ids.append(right_nbr)

    print(f"Res1: {part1(left_ids, right_ids)}")
    print(f"Res2: {part2(left_ids, right_ids)}")
