import re

PAGE_REGEX = re.compile(r"(\d+)\|(\d+)")


def part1(data) -> int:
    res = 0

    page_rules = [(int(x), int(y)) for x, y in PAGE_REGEX.findall("\n".join(data))]

    for line in data:
        if "," not in line:
            continue
        pages = list(map(int, line.split(",")))
        # We need to check if any of the page rules are violated,
        # This includes checking if both pages are in the list, so the rule actually applies
        # and if the first page is before the second page in the list
        if any(
            pages.index(x) > pages.index(y)
            for x, y in page_rules
            if x in pages and y in pages
        ):
            continue
        # We need to add the item in the center of the list to the result
        res += pages[len(pages) // 2]

    return res


def part2(data) -> int:
    res = 0

    page_rules = [(int(x), int(y)) for x, y in PAGE_REGEX.findall("\n".join(data))]

    for line in data:
        if "," not in line:
            continue
        pages = list(map(int, line.split(",")))
        valid_rules = [(x, y) for x, y in page_rules if x in pages and y in pages]
        invalid_update = False

        while True:
            invalid = False
            for x, y in valid_rules:
                if pages.index(x) < pages.index(y):
                    continue
                invalid = True
                invalid_update = True
                # rule doesn't match, so we need to apply the rule
                pages.remove(x)
                pages.insert(pages.index(y), x)
            if not invalid:
                break

        if invalid_update:
            res += pages[len(pages) // 2]

    return res


if __name__ == "__main__":
    with open("input") as f:
        data = f.read().splitlines()

    print(f"Res1: {part1(data)}")
    print(f"Res2: {part2(data)}")
