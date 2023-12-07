from pathlib import Path

source_folder = Path("src")
file_to_open = source_folder / "input_3rd_test.txt"

grid = open(file_to_open).read().splitlines()
coordinates = set()
numbers = []

def appendAdjacentNums(x,y,char,grid):
    tempNum = ""
    for x in [x-1,x,x+1]:
        for y in [y-1,y,y+1]:
            while grid[x-1][y].isdigit:
                tempNum += char
            number = int(tempNum)
            numbers.append(number)
                
def main():
	for x, row in enumerate (grid):
    	for y, char in enumerate (grid):
            if char.isdigit() or char == ".":
                continue
            else:
                getAdjacentNums(x,y,char,grid)
    print(sum(numbers))

main()
