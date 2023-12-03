"""
url: 
https://adventofcode.com/2023/day/1

input:
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

output: 
29 + 83 + 13 + 24 + 42 + 14 + 76 = 281

result for my input:
55260
"""

number_digit = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
}


def number(s: str) -> bool | int:
    """
    Returns false if there is no number in string, otherwise number
    """
    for k, v in number_digit.items():
        if k in s:
            return v
    return False


def digit_position(s: str, reverse: bool) -> (int, int):
    """
    Returns the first digit and its posion found in the string
    """
    s = s[::-1] if reverse else s
    for i, c in enumerate(s):
        if c.isdigit():
            return int(c), i
    return 0, len(s) + 1


def number_position(s: str, reverse: bool) -> (int, int):
    """
    Returns the first number and its position found in the string
    """
    for i in range(1, len(s)):
        n = number(s[-i:]) if reverse else number(s[: i + 1])
        if n:
            return n, i
    return 0, len(s) + 1


"""
Helper lambdas
"""
first = lambda digit, number: digit[0] if digit[1] < number[1] else number[0]
n = lambda front, back: int(str(front) + str(back))


def main() -> None:
    with open("input.txt", "r") as f:
        res = 0
        lines = f.read().split()
        for l in lines:
            front = first(digit_position(l, False), number_position(l, False))
            back = first(digit_position(l, True), number_position(l, True))
            res += n(front, back)
        print(res)


main()
