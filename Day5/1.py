"""
url:
https://adventofcode.com/2023/day/5
"""


def map_seeds(seeds: list[int], ranges: list[str]) -> dict[int, int]:
    d = {s: s for s in seeds}
    for r in ranges:
        destination, source, length = [int(_) for _ in r.split()]
        for s in seeds:
            if source <= s < source + length:
                d[s] = s - source + destination
    return d


with open("test.txt") as f:
    seeds = [int(s) for s in f.readline().replace("seeds:", "").split()]
    lines = [l.strip() for l in f.readlines() if l != "\n"]
    ranges = []
    print(f"seeds: {seeds}")
    for i, l in enumerate(lines):
        if l[0].isalpha() and not ranges:
            print(l)
        elif l[0].isalpha() and ranges:
            sm = map_seeds(seeds, ranges)
            seeds = sm.values()
            ranges = []
            print(sm)
            print(l)
        elif i == len(lines) - 1:
            ranges.append(l)
            sm = map_seeds(seeds, ranges)
            seeds = sm.values()
            print(sm)
            print(f"result: {min(seeds)}")
        else:
            ranges.append(l)
