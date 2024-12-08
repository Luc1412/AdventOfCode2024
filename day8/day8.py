from itertools import combinations

import numpy as np


def part1(data) -> int:
    antenna_locations = find_antennas(data)

    anomalies = set()
    # We now need to build vectors between all antennas of the same type
    for locations in antenna_locations.values():
        for loc1, loc2 in combinations(locations, 2):
            vector = np.array(loc1) - np.array(loc2)
            # We now need to find anomalies. loc1 - the vector and loc2 + the vector
            # show the anomaly locations
            anomaly1 = tuple(np.array(loc1) + vector)
            anomaly2 = tuple(np.array(loc2) - vector)
            # We now just need to check if the anomalies are in the grid
            if is_in_bounds(*anomaly1, data):
                anomalies.add(anomaly1)
            if is_in_bounds(*anomaly2, data):
                anomalies.add(anomaly2)

    return len(anomalies)


def part2(data) -> int:
    antenna_locations = find_antennas(data)

    anomalies = set()
    # We now need to build vectors between all antennas of the same type
    for locations in antenna_locations.values():
        for loc1, loc2 in combinations(locations, 2):
            vector = np.array(loc1) - np.array(loc2)

            for loc, sign in [(loc1, 1), (loc2, -1)]:
                anomaly = tuple(np.array(loc) + vector * sign)
                i = 1
                while is_in_bounds(*anomaly, data):
                    if data[anomaly[1]][anomaly[0]] == ".":
                        anomalies.add(anomaly)
                    i += 1
                    anomaly = tuple(np.array(loc) + vector * sign * i)

        # All antennae with at least 2 locations are also an anomaly
        if len(locations) > 1:
            anomalies.update(locations)

    return len(anomalies)


def find_antennas(data) -> dict[str, list[tuple[int, int]]]:
    # We need to find all antennas
    antenna_locations: dict[str, list[tuple[int, int]]] = {}
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == ".":
                continue
            antenna_locations.setdefault(data[y][x], []).append((x, y))

    return antenna_locations


def is_in_bounds(x, y, data) -> bool:
    return 0 <= x < len(data[0]) and 0 <= y < len(data)


if __name__ == "__main__":
    with open("input") as f:
        data = [list(l) for l in f.read().splitlines()]

    print(f"Res1: {part1(data)}")
    print(f"Res2: {part2(data)}")
