from pathlib import Path

source_folder = Path("src")
file_to_open = source_folder / "08_input_test.txt"

def part1():
    with open(file_to_open) as f:
        print(f.read())

part1()