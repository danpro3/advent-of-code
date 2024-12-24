
# %%
# lines = open('inputs/input_22_test.txt','r').read().splitlines()
lines = open('inputs/input_22.txt','r').read().splitlines()
# print(lines)
# %% part 1 ------------------------------------------------------------------
def next_rando(x):
    x = ((x * 64) ^ x) % 16777216
    x = ((x // 32) ^ x) % 16777216
    x = ((x * 2048) ^ x) % 16777216
    return x

totals = 0
for line in lines:
    x = int(line)
    for i in range(2000):
        x = next_rando(x)
    totals += x
print(f'totals = {totals}')

# %% part 2 -----------------------------------------------------------------
from collections import defaultdict

def build_price_list():
    # build the price list
    all_P = []; all_dP = []
    for line in lines:
        P = []; dP = []
        x = int(line)
        for i in range(2000):
            s = x % 10
            x = next_rando(x)
            # print(x)
            P.append(x % 10)
            dP.append(x % 10 - s % 10)
        all_P.append(P); all_dP.append(dP)
    # print(lines)
    # print(all_P)
    # print(all_dP)
    return all_P, all_dP

def calc_bananas(checklist):
    bananas = 0
    # checklist = [-1,-1,0,2]
    for k,_ in enumerate(lines):
        i = 0
        while checklist != all_dP[k][i:i+4] and i+4 < len(all_dP[k]):
            i += 1
        if i+4 < len(all_dP[k]):
            bananas += all_P[k][i+3]
            # print(f'{k}, price = {all_P[k][i+3]}')
    return bananas

# main
quads = defaultdict(int)
all_P, all_dP = build_price_list()
for k in range(len(all_dP)):
    set_for_one_buyer = set()
    for i in range(len(all_dP[k])-3):
            if tuple(all_dP[k][i:i+4]) not in set_for_one_buyer:
                set_for_one_buyer.add(tuple(all_dP[k][i:i+4]))
                quads[tuple(all_dP[k][i:i+4])] += all_P[k][i+3]

print(f'length of quads = {len(quads)}')
# print(max(quads.values()))
key = max(quads, key=quads.get)
print(f'max = {quads[key]} bananas with pattern: {key}')
