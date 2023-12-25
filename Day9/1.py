"""
url:
https://adventofcode.com/2023/day/9
"""


def sequence(s: list[int]) -> int:
    if all(n == 0 for n in s):
        return 0
    return s[-1] + sequence([b - a for (a, b) in zip(s[:-1], s[1:])])


with open("input.txt") as f:
    lines = [[int(n) for n in l.split()] for l in f.readlines()]
    result = sum([sequence(s) for s in lines])
    print(result)
