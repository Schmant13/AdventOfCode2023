from pathlib import Path

source_folder = Path("src")
file_to_open = source_folder/"08_input.txt"

def part1():
    with open(file_to_open) as f:
        positions = {}
        #instructions are the first lines e.g. "RLRLLR"
        instructions, _, *block = f.read().splitlines()
        for line in block:
            destination, direction = line.split(" = ")
            positions[destination] = direction[1:-1].split(", ")
    
        current = "AAA"
        step_count = 0

        while current != "ZZZ":
            current = positions[current][0 if instructions[0]== "L" else 1 ]
            instructions = instructions[1:] + instructions[0]
            step_count += 1
        print("steps: ", step_count)

part1()

def part2():
    with open(file_to_open) as f:
        positions = {}
        #instructions are the first lines e.g. "RLRLLR"
        instructions, _, *block = f.read().splitlines()
        for line in block:
            destination, direction = line.split(" = ")
            positions[destination] = direction[1:-1].split(", ")
    
        current = "AAA"
        step_count = 0

        while current != "ZZZ":
            current = positions[current][0 if instructions[0]== "L" else 1 ]
            instructions = instructions[1:] + instructions[0]
            step_count += 1
        print("steps: ", step_count)

part2()  