# %% 
# load input
import re
filestr = '125 17'
filestr = '30 71441 3784 580926 2 8122942 0 291' # main input
# filestr = '30'
stones = filestr.split(' ')
print(stones)
# _=[print(x) for x in grid]
# %% part 1
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
N_BLINKS = 27
blinks = [x for x in range(1,N_BLINKS+1)]
nstones = []
for i in range(N_BLINKS):
    blink()
    print(f'stones: {stones}')
    nstones.append(len(stones))
    print(f'Blink number: {i+1} Num stones = {len(stones)}')

# %% plot the number of stones vs blinks
import matplotlib.pyplot as plt
print(blinks)
print(nstones)
_=[print(nstones[s]) for s in range(0,len(nstones))]
_=[print(int(nstones[s+1])-int(nstones[s])) for s in range(0,len(nstones)-1)]
plt.figure()
plt.plot(blinks,nstones,'o')
plt.grid()
# %% part 2 - not working yet
from heapq import heapify, heappush, heappop

def blink2(todo):
    blinks, stone, n = heappop(todo)
    if blinks == N_BLINKS:
        allstones.append(stone)
        return todo
    # if stone in cache:
    #     cache[stone] += n
    #     return
    # else:
    #     cache[stone] = n
    if stone == '0':
        heappush(todo, (blinks + 1, '1', n+1))
    elif len(stone) % 2 == 0:
        left = stone[0:int(len(stone)/2)]
        right = str(int(stone[int(len(stone)/2):]))
        heappush(todo, (blinks + 1, left, n+1))
        heappush(todo, (blinks + 1, right, n+1))
    else:
        heappush(todo, (blinks + 1, str(int(stone)*2024), n+1))

filestr = '30 71441 3784 580926 2 8122942 0 291' # main input
N_BLINKS = 25

stones = filestr.split(' ')
cache = {}
todo = []
allstones = []
for stone in stones:
    heappush(todo, (0, stone, 1))
print(f'num stones: {len(stones)}, todo = {todo}')
while todo:
    blink2(todo)

print(f'n blinks = {N_BLINKS}, length allstones: {len(allstones)}')
# print(allstones)
# %% part 2 recursion

def blink3(stone, blinks_remain):
    if blinks_remain == 0:
        return 1
    if (stone, blinks_remain) in cache:
        return cache[stone, blinks_remain]
    if stone == '0':
        cache[stone, blinks_remain] = blink3('1', blinks_remain - 1)
    elif len(stone) % 2 == 0:
        left = stone[0:int(len(stone)/2)]
        right = str(int(stone[int(len(stone)/2):]))
        cache[stone, blinks_remain] = blink3(left, blinks_remain - 1) + blink3(right, blinks_remain - 1)
    else:
        cache[stone, blinks_remain] = blink3(str(int(stone)*2024), blinks_remain - 1)
    return cache[stone, blinks_remain]

filestr = '30 71441 3784 580926 2 8122942 0 291' # main input
N_BLINKS = 75

stones = filestr.split(' ')
cache = {}
total_stones = 0
for stone in stones:
    total_stones += blink3(stone,N_BLINKS)

print(f'n blinks = {N_BLINKS}, length stones= {total_stones}')

