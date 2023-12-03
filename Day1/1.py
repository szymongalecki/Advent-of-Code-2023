"""
url: 
https://adventofcode.com/2023/day/1

input:
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

output: 
12 + 38 + 15 + 77 = 142

result for my input:
55123
"""


def first_digit(s: str):
    for c in s:
        if c.isdigit():
            return c


def number(d1: str, d2: str):
    return int(d1 + d2)


def main():
    with open("input.txt", "r") as f:
        res = 0
        lines = f.read().split()
        for l in lines:
            d1 = first_digit(l)
            d2 = first_digit(l[::-1])
            n = number(d1, d2)
            res += n
        print(res)


main()
