from pathlib import Path

data_folder = Path("src")
file_to_open = data_folder / "1st_input.txt"

f = open(file_to_open)
#calibration values of a line
values = []
#calibration values of all lines
AllValues = []
#digits in words with corresponding number
num_map = {  
'one': '1',  
'two': '2',  
'three': '3',  
'four': '4',  
'five' : '5',  
'six': '6',  
'seven': '7',  
'eight': '8',  
'nine': '9'  
}  

for line in f:
    #word holds all letters of a line
    word = ''
    for char in line:
        if char.isdigit():
            dig = char
            values.append(dig)
        else:
            word += char
            for k,v in num_map.items():
                if word.endswith(k):
                    dig = v
                    values.append(dig)
    #int value to append to the final list (AllValues)
    num = int((str(values[0])+str(values[-1])))
    AllValues.append(num)
    values.clear()

all = sum(AllValues)
print('All calibration values: ', AllValues)
print('All calibration values together: ', all)
f.close