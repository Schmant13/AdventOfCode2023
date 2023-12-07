from pathlib import Path

source_folder = Path("src")
file_to_open = source_folder / "input_3rd_test.txt"

grid = open(file_to_open).read().splitlines()
coordinates = set()

class Grid:
    for x, row in enumerate(grid):
        for y, column in enumerate (row):
            pos_x = x
            pos_y = y
        pass
