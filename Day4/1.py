"""
url: 
https://adventofcode.com/2023/day/4

input:
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

output:
13

explanation:
The first match makes the card worth one point
and each match after the first doubles the point value of that card.

result for my input:
23847
"""


def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        res = 0
        for l in lines:
            _, cards = l.split(":")
            winning, have = cards.split("|")
            winning = [int(w) for w in winning.split()]
            have = [int(h) for h in have.split()]
            p = 1
            points = 0
            for h in have:
                if h in winning:
                    points = p
                    p *= 2
            print(f"{winning=}, {have=}, {points=}")
            res += points
    print(res)


main()
