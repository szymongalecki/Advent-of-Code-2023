"""
url:
https://adventofcode.com/2023/day/7
"""


def type(hand: str) -> None:
    h = "".join(sorted([str(hand.count(c)) for c in hand], reverse=True))
    match h:
        case "55555":  # Five of a kind
            return 6
        case "44441":  # Four of a kind
            return 5
        case "33322":  # Full house
            return 4
        case "33311":  # Three of a kind
            return 3
        case "22221":  # Two pair
            return 2
        case "22111":  # One pair
            return 1
        case "11111":  # High card
            return 0


def strength(hand: str):
    card_strength = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    return (type(hand), [card_strength[c] if c.isalpha() else int(c) for c in hand])


def main():
    with open("input.txt") as f:
        hands = [[l.split()[0], int(l.split()[1])] for l in f.readlines()]
        sorted_hands = sorted(hands, key=lambda h: strength(h[0]))
        mul = 1
        res = 0
        for h in sorted_hands:
            res += h[1] * mul
            mul += 1
        print(res)


main()
