# %% 
# load input
import re
filestr = '125 17'
filestr = '30 71441 3784 580926 2 8122942 0 291' # main input
filestr = '30'
stones = filestr.split(' ')
print(stones)
# _=[print(x) for x in grid]
# %%
def blink():
    s = 0        
    while s < len(stones):
        # if stones[s] in cache:


        if stones[s] == '0':
            stones[s] = '1'
            s += 1
        elif len(stones[s]) % 2 == 0:
            temp = stones[s]
            stones[s] = temp[0:int(len(temp)/2)]
            stones.insert(s+1, temp[int(len(temp)/2):])
            stones[s+1] = str(int(stones[s+1]))
            s += 2
        else:
            stones[s] = str(int(stones[s])*2024)
            s += 1

stones = filestr.split(' ')
N_BLINKS = 26
blinks = [x for x in range(1,N_BLINKS+1)]
nstones = []
cache = {}
for i in range(N_BLINKS):
    blink()
    # print(f'stones: {stones}')
    nstones.append(len(stones))
    print(f'Blink number: {i+1} Num stones = {len(stones)}')

# %%
import matplotlib.pyplot as plt
print(blinks)
print(nstones)
_=[print(nstones[s]) for s in range(0,len(nstones))]
_=[print(int(nstones[s+1])-int(nstones[s])) for s in range(0,len(nstones)-1)]
plt.figure()
plt.plot(blinks,nstones,'o')
plt.grid()
# %%
