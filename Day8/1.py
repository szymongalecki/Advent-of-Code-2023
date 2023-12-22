with open("input.txt") as f:
    instructions, network = f.read().split("\n", 1)
    network = network.strip().split("\n")
    network = [
        n.replace("=", "").replace("(", "").replace(")", "").replace(",", "").split()
        for n in network
    ]
    network = {n[0]: {"L": n[1], "R": n[2]} for n in network}
    instructions = [i for i in instructions]
    node = "AAA"
    steps = 0
    while node != "ZZZ":
        i = instructions.pop(0)
        instructions.append(i)
        print(node, network[node], i)
        node = network[node][i]
        steps += 1
    print(steps)
