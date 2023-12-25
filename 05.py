from pathlib import Path

src_folder = Path("src")
file_to_open = src_folder / "input_5th.txt"

def first():
    with open(file_to_open) as f:
        seeds, *blocks = f.read().split("\n\n")
        seed_split = seeds.split(": ")[1].split()
        seeds = list(map(int, seed_split))

        for block in blocks:
            ranges = []
            for line in block.splitlines()[1:]:
                ranges.append(list(map(int, line.split())))
            new = []
            for seed in seeds:
                for a, b, c in ranges:
                    if b <= seed < b + c:
                        new.append(seed - b + a)
                        break
                else:
                    new.append(seed)
            seeds = new

        print(min(seeds))
#first()

def second():
    with open(file_to_open) as f:
    seeds, *blocks = f.read().split("\n\n")
    seed_split = seeds.split(": ")[1].split()
    temp_seed = []
    for i, s in seed_split:
        if len(temp_seed) < 2:
            temp_seed.append(s)
        else:
            seeds += temp_seed

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        for seed in seeds:
            for a, b, c in ranges:
                if b <= seed < b + c:
                    new.append(seed - b + a)
                    break
            else:
                new.append(seed)
        seeds = new
    print(min(seeds))

second()