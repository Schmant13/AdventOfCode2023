from pathlib import Path

src_folder = Path("src")
file_to_open = src_folder / "input_4th.txt"
f = open(file_to_open)

total = 0

for lines in f:
    card = 0
    #split "Card...:" from numbers
    line = lines.split(':')
    #split winning numbers from own numbers
    nums = line[1].strip().split(" | ")
    winningNums = nums[0].strip().split()
    ownNums = nums[1].strip().split()
    #check if own numbers in winning numbers + add to temporal variable "card")
    for num in ownNums:
        if num in winningNums:
            if card == 0:
                card += 1
                print(num, winningNums)
                print(card)
            else:
                card *= 2
                print(num, winningNums)
                print(card)
    total += card
    
print(total)
                