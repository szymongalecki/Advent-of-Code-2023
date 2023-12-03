"""
url: 
https://adventofcode.com/2023/day/2

input:
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

explanation:
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.


output:
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. 
The power of the minimum set of cubes in game 1 is 48. 
In games 2-5 it was 12, 1560, 630, and 36, respectively. 
Adding up these five powers produces the sum 2286

result for my input:
66363
"""

from math import prod as product


def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        res = 0
        for l in lines:
            print(l)
            cubes = {"red": 0, "green": 0, "blue": 0}
            id, games = l.split(":")
            id = int(id.replace("Game ", ""))
            for g in games.split(";"):
                for d in g.split(","):
                    v, k = d.strip().split()
                    print(f"{v}, {k}")
                    if int(v) > cubes[k]:
                        cubes[k] = int(v)
                print("- - - - - - - -")
            print(cubes)
            res += product(cubes.values())
    print(res)


main()
