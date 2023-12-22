"""
url: 
https://adventofcode.com/2023/day/6

input:
Time:      7  15   30
Distance:  9  40  200

output:
288 = 4 * 8 * 9

explanation:
Result is a product of number of ways to win each race.

result for my input:
1108800
"""


def ways(t: int, d: int) -> int:
    c = 1  # charge time [ms]
    s = 1  # speed [mm / ms]
    w = 0  # ways to win
    while c != t:
        if c + d / s < t:
            w += 1
        c += 1
        s += 1
    return w


with open("input.txt") as f:
    time, distance = f.read().split("\n")
    time = map(int, time.replace("Time:", "").split())
    distance = map(int, distance.replace("Distance:", "").split())
    res = 1
    for t, d in zip(time, distance):
        res *= ways(t, d)
    print(res)
