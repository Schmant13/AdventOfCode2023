from pathlib import Path

data_folder = Path("src")
file_to_open = data_folder / "input_2nd.txt"

#total possible games
t = 0
#game ID
i = 0

with open(file_to_open) as f:
    for line in f:
        gs = line.strip().split(': ')[1].split('; ')
        i += 1
        #count: won/possible sub sets
        sw = 0
        #count: all subsets
        sb = 0
        mM = {'red':0, 'green':0, 'blue':0}
        for g in gs:
            M = {'red': 0, 'green': 0, 'blue': 0}
            for c in g.split(', '):
                sb += 1
                #spliting number and color
                a, b = c.split()
                M[b] = int(a)
                # checking if a subset is possible
                if M['red'] > 12 or M['green'] > 13 or M['blue'] > 14:
                    break
                else:
                    sw += 1
        if sb == sw:
            t += i

    # 1st Part
    print('Sum of the IDs of possible games: ', t)
