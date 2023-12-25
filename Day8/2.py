from math import lcm

with open("input.txt") as f:
    instructions, network = f.read().split("\n", 1)
    network = network.strip().split("\n")
    network = [
        n.replace("=", "").replace("(", "").replace(")", "").replace(",", "").split()
        for n in network
    ]
    network = {n[0]: {"L": n[1], "R": n[2]} for n in network}
    instructions = [i for i in instructions]
    starting_nodes = [k for k in network.keys() if k[-1] == "A"]
    cycles = []
    steps = 0

    for node in starting_nodes:
        curr = node
        while not curr.endswith("Z"):
            steps += 1
            i = instructions.pop(0)
            instructions.append(i)
            curr = network[curr][i]
        print(f"{node} -> {curr} = {steps}")
        cycles.append(steps)
        steps = 0

    print(cycles)
    print(lcm(*cycles))
