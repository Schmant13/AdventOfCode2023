from pathlib import Path

src_folder = Path("src")
file_to_open = src_folder / "input_4th_test.txt"
f = open(file_to_open).readline()

for lines in f:
    line = lines.split(':')
    print(line)
