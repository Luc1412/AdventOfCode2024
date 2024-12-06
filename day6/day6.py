from enum import Enum
from itertools import cycle
from typing import NamedTuple


class CursorFacing(Enum):
    NORTH = "^"
    EAST = ">"
    SOUTH = "v"
    WEST = "<"


class CursorPosition(NamedTuple):
    x: int
    y: int


class Cursor(NamedTuple):
    position: CursorPosition
    facing: CursorFacing


DIRECTION_MAP = {
    CursorFacing.NORTH: (0, -1),
    CursorFacing.EAST: (1, 0),
    CursorFacing.SOUTH: (0, 1),
    CursorFacing.WEST: (-1, 0),
}


def part1(data) -> int:
    cursor = get_cursor(data)
    visted_positions: set[CursorPosition] = set()

    while True:
        dx, dy = DIRECTION_MAP[cursor.facing]
        next_position = CursorPosition(cursor.position.x + dx, cursor.position.y + dy)

        # If we're out of bounds, break
        if not (
            0 <= next_position.y < len(data)
            and 0 <= next_position.x < len(data[next_position.y])
        ):
            break

        # If we're about to hit an obstacle, turn right
        if data[next_position.y][next_position.x] == "#":
            cursor_facing_cycle = cycle(CursorFacing)
            for cursor_facing in cursor_facing_cycle:
                if cursor_facing is cursor.facing:
                    cursor = Cursor(cursor.position, next(cursor_facing_cycle))
                    break
            continue

        visted_positions.add(cursor.position)
        cursor = Cursor(next_position, cursor.facing)

    # We want all visted positions, including the starting one
    return len(visted_positions) + 1


def get_cursor(data) -> Cursor:
    cursor_values = [c.value for c in CursorFacing]
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] in cursor_values:
                return Cursor(CursorPosition(x, y), CursorFacing(data[y][x]))


def part2(data) -> int:
    res = 0

    return res


if __name__ == "__main__":
    with open("input") as f:
        data = [list(line) for line in f.read().splitlines()]

    print(f"Res1: {part1(data)}")
    print(f"Res2: {part2(data)}")
