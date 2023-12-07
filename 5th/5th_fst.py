from pathlib import Path

src_folder = Path("src")
file_to_open = src_folder / "input_5th_test.txt"
f = open(file_to_open)

M = {seed: None, soil: None, fertilizer: None, water: None, light: None, temperature: None, humidity: None, location: None}
seed_info = []

def main():
    for line in f:
        if line.startswith("seeds"):
            seed_line = line.split(": )
            seeds = seed_line[1].strip.split()
            sort(seed)
        elif line =="":
            continue
        else:
            pass
            
            
            

