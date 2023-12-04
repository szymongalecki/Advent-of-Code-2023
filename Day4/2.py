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
30

explanation:
You win copies of the scratchcards below the winning card,
equal to the number of matches. 
So, if card 10 were to have 5 matching numbers, 
you would win one copy each of cards 11, 12, 13, 14, and 15.

result for my input:
8570000
"""


def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        multipliers = {n: 1 for n in range(1, len(lines) + 1)}
        for i, l in enumerate(lines):
            _, cards = l.split(":")
            winning, have = cards.split("|")
            winning = [int(w) for w in winning.split()]
            have = [int(h) for h in have.split()]
            scratch = 0
            # count scratchards
            for h in have:
                if h in winning:
                    scratch += 1
            print(f"{winning=}, {have=}, {scratch=}")
            # increment multipliers this many times
            for _ in range(multipliers[i + 1]):
                n = 1
                s = scratch
                while s > 0:
                    if i + 1 + n in multipliers:
                        multipliers[i + 1 + n] += 1
                    s -= 1
                    n += 1
            print(f"{multipliers=}\n")
        print(sum(multipliers.values()))


main()
