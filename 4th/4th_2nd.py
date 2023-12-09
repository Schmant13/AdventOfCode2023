from pathlib import Path

src_folder = Path("src")
file_to_open = src_folder / "input_4th.txt"
f = open(file_to_open)

total = 0
cardMultiplier = 0

for lines in f:
    wins = 0
    #split "Card...:" from numbers
    line = lines.split(':')
    #split winning numbers from own numbers
    nums = line[1].strip().split(" | ")
    winningNums = nums[0].strip().split()
    ownNums = nums[1].strip().split()
    #check if own numbers in winning numbers + add to temporal variable "card")
    for num in range ownNums:
        if num in winningNums:
            wins +=1
                