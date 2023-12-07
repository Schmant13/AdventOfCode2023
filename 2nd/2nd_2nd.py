from pathlib import Path

data_folder = Path("src")
file_to_open = data_folder / "input_2nd.txt"

#game ID
i = 0
#total power, sum of every game's power
tp = 0

with open(file_to_open) as f:
    for line in f:
        gs = line.strip().split(': ')[1].split('; ')
        i += 1
        mM = {'red':0, 'green':0, 'blue':0}
        for g in gs:
            M = {'red': 0, 'green': 0, 'blue': 0}
            for c in g.split(', '):
                #spliting number and color
                a, b = c.split()
                M[b] = int(a)
            for k in M:
                mM[k] = max(M[k], mM[k])
        #power of one game
        p = mM['red']*mM['green']*mM['blue']
        tp += p

    # 2nd Part
    print("total power (sum of every game's power: ", tp)