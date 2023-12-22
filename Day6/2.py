"""
url: 
https://adventofcode.com/2023/day/6

input:
Time:      7  15   30
Distance:  9  40  200

interpretation of input:
Time:      71530
Distance:  940200

output:
71503

explanation:
Result is a number of ways to win the race.

result for my input:
36919753
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
    time = int(time.replace("Time:", "").replace(" ", ""))
    distance = int(distance.replace("Distance:", "").replace(" ", ""))
    print(ways(time, distance))
