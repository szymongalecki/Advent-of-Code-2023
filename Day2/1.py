"""
url:
https://adventofcode.com/2023/day/2

input:
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

constraints:
- 12 red cubes
- 13 green cubes
- 14 blue cubes

output:
1 + 2 + 5 = 8

result for my input:
2369
"""

constraints = {"red": 12, "green": 13, "blue": 14}


def main():
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]
        res = 0
        for l in lines:
            print(l)
            id, games = l.split(":")
            id = int(id.replace("Game ", ""))
            possible = True
            for g in games.split(";"):
                for d in g.split(","):
                    v, k = d.strip().split()
                    print(f"{v}, {k}")
                    if int(v) > constraints[k]:
                        possible = False
                print("- - - - - - - -")
            print(f"{possible=}, {id=}\n")
            if possible:
                res += id
        print(res)


main()
