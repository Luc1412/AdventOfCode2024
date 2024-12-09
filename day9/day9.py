def part1(data) -> int:
    disk = []
    for i, amount in enumerate(data):
        id_ = i / 2
        # if id is an integer, it represents a block of data. We need to extend the disk with that block
        # if id is a float, it represents how much space is free.
        disk.extend([int(id_)] * amount if id_.is_integer() else [None] * amount)

    for i, value in enumerate(disk):
        if value is not None:
            continue
        # If we find a free space, we need to take the last element of the disl (that is not None) and put it in the free space
        for j in range(len(disk) - 1, 0, -1):
            if disk[j] is not None:
                disk[i], disk[j] = disk[j], None
                break
        # If all last elements are None, we can stop
        if all(x is None for x in disk[i + 2 :]):
            break
    return sum(i * v for i, v in enumerate(disk) if v is not None)


def part2(data) -> int:
    blocks = {int(i / 2): amount for i, amount in enumerate(data) if i % 2 == 0}

    disk = []
    for i, amount in enumerate(data):
        id_ = i / 2
        if id_.is_integer() and id_ in blocks:
            disk.extend([int(id_)] * amount)
            blocks.pop(int(id_))
        # We got space, lets find the proper block to insert
        else:
            for block_id in reversed(list(blocks.keys())):
                block_size = blocks[block_id]
                if block_size > amount:
                    continue
                disk.extend([block_id] * block_size)
                amount -= block_size
                del blocks[block_id]
            disk.extend([None] * amount)
    return sum(i * v for i, v in enumerate(disk) if v is not None)


if __name__ == "__main__":
    with open("input") as f:
        data = list(map(int, f.read()))

    print(f"Res1: {part1(data)}")
    print(f"Res2: {part2(data)}")
