from pathlib import Path

data_folder = Path("src")
file_to_open = data_folder / "1st_input.txt"

f = open(file_to_open)

#calibration values of a line
values = []
#calibration values of all lines
AllValues = []
for line in f:
    for character in line:
        if character.isdigit():
            values.append(character)
        else:
            continue
    n = len(values)
    #only appending the first and the last digit of a line
    item = int(str(values[0])+str(values[n-1]))
    AllValues.append(item)
    values.clear()

print("All calibration Values:", AllValues)    
#adding all calibration values + printing
sum = sum(AllValues)
print("Sum of all calibration values:", sum)
f.close()