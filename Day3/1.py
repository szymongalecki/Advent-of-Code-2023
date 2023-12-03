"""
url: 
https://adventofcode.com/2023/day/3

input:
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

output:
sum of numbers adjacent to symbols = 4361
114 and 58 are not included

result for my input:
539713
"""


class Grid:
    def __init__(self, file: str) -> None:
        """
        Creates a grid from file, sets its dimensions
        """
        with open(file, "r") as f:
            self.grid = [l.strip() for l in f.readlines()]
            self.X = len(self.grid[0]) - 1
            self.Y = len(self.grid) - 1

    def adjacent(self, x: int, y: int) -> str:
        """
        Returns a string of adjacent characters, clockwise
        """
        a = ""
        # Top
        if y > 0:
            a += self.grid[y - 1][x]
        # Right
        if x < self.X:
            a += self.grid[y][x + 1]
        # Right Top
        if x < self.X and y > 0:
            a += self.grid[y - 1][x + 1]
        # Right Bottom
        if x < self.X and y < self.Y:
            a += self.grid[y + 1][x + 1]
        # Bottom
        if y < self.Y:
            a += self.grid[y + 1][x]
        # Left Bottom
        if x > 0 and y < self.Y:
            a += self.grid[y + 1][x - 1]
        # Left
        if x > 0:
            a += self.grid[y][x - 1]
        # Left Top
        if x > 0 and y > 0:
            a += self.grid[y - 1][x - 1]
        return a

    def symbol(self, s: str) -> bool:
        """
        Returns True if special symbol was found in string, otherwise False
        """
        for c in s:
            if not c.isdigit() and c != ".":
                return True
        return False

    def traverse(self):
        """
        Traverses grid and returns the sum of adjacent numbers
        """
        res = 0
        for y in range(self.Y + 1):
            a = ""
            n = ""
            for x in range(self.X + 1):
                p = self.grid[y][x]
                # digit
                if p.isdigit():
                    n += p
                    a += self.adjacent(x=x, y=y)
                    # last digit in a row
                    if x == self.X and self.symbol(a):
                        print(f"+ {int(n)}")
                        res += int(n)
                # not digit
                else:
                    if self.symbol(a):
                        print(f"+ {int(n)}")
                        res += int(n)
                    # reset adjacent string 'a' and numstring 'n'
                    a = ""
                    n = ""

            print("- - - - - - - - - - - - ")
        print(res)


def main():
    grid = Grid("input.txt")
    grid.traverse()


main()
