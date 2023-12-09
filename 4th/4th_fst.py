from pathlib import Path

src_folder = Path("src")
file_to_open = src_folder / "input_4th_test.txt"
f = open(file_to_open)

def part1():
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
#part1()

def part2():
    multipliers = []
    
    for time in range (current_multiplier):
        for line_index, lines in enumerate (f):
            #split "Card...:" from numbers
            line = lines.split(':')
            #split winning numbers from own numbers
            nums = line[1].strip().split(" | ")
            winningNums = nums[0].strip().split()
            ownNums = nums[1].strip().split()
            #check if own numbers in winning numbers + add to temporal variable "card")
            for index, num in enumerate (ownNums):
                score = 1
                if num in winningNums:
                    score += 1
                    if len(multipliers) == 0:
                        multipliers.append(score)
                    elif score >= len(multipliers):
                        multipliers[index] += score
                    else:
                        multipliers.append(2)
            current_multiplier_index = line_index + 1
            current_multiplier = multipliers[current_multiplier_index]