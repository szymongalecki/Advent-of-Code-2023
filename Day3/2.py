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
sum of products, of two numbers adjacent to '*' symbol
467*35 + 755*598 = 467835

result for my input:
84159075
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
            self.stars = {}

    def adjacent_star(self, x: int, y: int) -> list[tuple[int, int]]:
        """
        Returns a list of coordinations of adjacent stars
        """
        stars = []
        if y > 0 and self.grid[y - 1][x] == "*":
            stars.append((y - 1, x))
        if x < self.X and self.grid[y][x + 1] == "*":
            stars.append((y, x + 1))
        # Right Top
        if x < self.X and y > 0 and self.grid[y - 1][x + 1] == "*":
            stars.append((y - 1, x + 1))
        # Right Bottom
        if x < self.X and y < self.Y and self.grid[y + 1][x + 1] == "*":
            stars.append((y + 1, x + 1))
        # Bottom
        if y < self.Y and self.grid[y + 1][x] == "*":
            stars.append((y + 1, x))
        # Left Bottom
        if x > 0 and y < self.Y and self.grid[y + 1][x - 1] == "*":
            stars.append((y + 1, x - 1))
        # Left
        if x > 0 and self.grid[y][x - 1] == "*":
            stars.append((y, x - 1))
        # Left Top
        if x > 0 and y > 0 and self.grid[y - 1][x - 1] == "*":
            stars.append((y - 1, x - 1))
        return stars

    def traverse(self):
        """
        Traverses grid and returns the sum of products, of numbers adjacent to a star symbol - '*'
        """
        res = 0
        for y in range(self.Y + 1):
            n = ""
            stars = []
            for x in range(self.X + 1):
                c = self.grid[y][x]
                # digit
                if c.isdigit():
                    n += c
                    stars += self.adjacent_star(x=x, y=y)
                # not digit
                if not c.isdigit() or x == self.X:
                    for s in set(stars):
                        if s not in self.stars:
                            # star is adjacent to one number
                            self.stars[s] = int(n)
                        else:
                            # star is adjacent to two numbers
                            print(f"{int(n)} * {self.stars[s]}")
                            res += self.stars[s] * int(n)
                            self.stars.pop(s)
                    n = ""
                    stars = []
            print(f"- - - - - - - - - - - - {y+1}")
        print(f"{res=}")


def main():
    grid = Grid("input.txt")
    grid.traverse()


main()
