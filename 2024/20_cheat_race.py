# %% read file
# filestr = open("inputs/input_20_test.txt", "r").read()
filestr = open('inputs/input_20.txt','r').read()
grid = filestr.splitlines()
rows = len(grid)
cols = len(grid[0])
idx = filestr.index("S")
S = (idx // (cols + 1), idx % (cols + 1))
idx = filestr.index("E")
E = [idx // (cols + 1), idx % (cols + 1)]
print(f"start = {S}, end = {E}")
# _=[print(x) for x in grid]  # print as strings
grid = [list(x) for x in grid]  # make individual chars
# _=[print(''.join(x)) for x in grid]  # print as strings

# %% part 1
from collections import defaultdict
from heapq import heapify, heappush, heappop

def move(todo,can_cheat):
    steps, r, c, dir, cheated = heappop(todo)
    if can_cheat:
        if cheated:
            if (r, c) in path:
                allsteps.append(steps + maxsteps - path[(r,c)])
                return steps, todo       
    else:
        path[(r,c)] = steps
    # print(f'grid [{r}][{c}] = {grid[r][c]}')
    if grid[r][c] == "E":
        # todo = [] # quit after finding the first ending
        print(f'Done. r,c = {r,c}, steps = {steps}, cheated: {cheated}')
        allsteps.append(steps + maxsteps - path[(r,c)])
        return steps, todo
    for d in dirs:
        dr, dc = d
        if dir[0] + dr != 0 or dir[1] + dc != 0: # don't reverse
            if 0 <= r + dr < rows and 0 <= c + dc < cols:
                if grid[r + dr][c + dc] in [".", "E"]:
                    heappush(todo, (steps + 1, r + dr, c + dc, d, cheated))
        # check for cheat
        if can_cheat and not cheated and 0 <= r + 2*dr < rows and 0 <= c + 2*dc < cols:
            if grid[r + 2*dr][c + 2*dc] in [".", "E"]:
                heappush(todo, (steps + 2, r + 2*dr, c + 2*dc, d, True))
    return steps, todo

def find_paths(allsteps,can_cheat):
    todo = []
    heappush(todo, (0, S[0], S[1], (0,0), False))
    while todo:
        steps, todo = move(todo,can_cheat)
    if can_cheat:
        return allsteps
    else:
        return steps

# main
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
path = defaultdict()
can_cheat = False # run the first one thru to build the path
allsteps = []
maxsteps = 0
maxsteps = find_paths(allsteps,can_cheat)
print(f'maxsteps = {maxsteps}')

allsteps = []
can_cheat = True # now apply cheating
allsteps = find_paths(allsteps,can_cheat)
# print(allsteps)

savings = defaultdict(int)
savethreshold = 100
singlesavings = 0
for i,s in enumerate(allsteps):
    savings[maxsteps-allsteps[i]] += 1
    if maxsteps-allsteps[i] >= savethreshold:
        singlesavings += 1

print('part 1: 2 picosecond cheat')
# _ = [print(f"There are {savings[x]} cheats that save {x} steps") for x in savings if x > 0]
print(f'To save at least {savethreshold} steps, there are {singlesavings} cheats')


# %% part 2

def move2(todo,can_cheat):
    steps, r, c, dir, cheated, (r0,c0,r1,c1) = heappop(todo)
    if (r0,c0,r1,c1,steps) in cache:
        return steps, todo
    else:
        cache.add((r0,c0,r1,c1,steps))
    if can_cheat:
        if cheated:
            if (r, c) in path:
                allsteps.append(steps + maxsteps - path[(r,c)])
                return steps, todo       
    else:
        path[(r,c)] = steps
    # print(f'grid [{r}][{c}] = {grid[r][c]}')
    if grid[r][c] == "E":
        # todo = [] # quit after finding the first ending
        print(f'Done. r,c = {r,c}, steps = {steps}, cheated: {cheated}')
        allsteps.append(steps + maxsteps - path[(r,c)])
        return steps, todo
    for d in dirs:
        dr, dc = d
        if dir[0] + dr != 0 or dir[1] + dc != 0: # don't reverse
            if 0 <= r + dr < rows and 0 <= c + dc < cols:
                if grid[r + dr][c + dc] in ['.', 'E']:
                    heappush(todo, (steps + 1, r + dr, c + dc, d, cheated, (r0,c0,r1,c1)))
        # check for cheat
        if not cheated:
            for dr in range(-20,21):
                for dc in range(-20,21):
                    if (abs(dr) + abs(dc) <= 20 and
                    0 <= r + dr < rows and 0 <= c + dc < cols):
                        if grid[r + dr][c + dc] in ['.','E']:
                            heappush(todo, (steps + abs(dr) + abs(dc), r + dr, c + dc, d, True, (r,c,r+dr,c+dc)))
    return steps, todo

def find_paths2(allsteps,can_cheat):
    todo = []
    heappush(todo, (0, S[0], S[1], (0,0), False, (-2,-2,-2,-2)))
    while todo:
        steps, todo = move2(todo,can_cheat)
    return allsteps

# main
cache = set()
allsteps = []
can_cheat = True # now apply cheating
allsteps = find_paths2(allsteps,can_cheat)
# print(allsteps)

savings = defaultdict(int)
savethreshold = 100
singlesavings = 0
for i,s in enumerate(allsteps):
    savings[maxsteps-allsteps[i]] += 1
    if maxsteps-allsteps[i] >= savethreshold:
        singlesavings += 1

print('part 2: 20 picosecond cheat')
# _ = [print(f"There are {savings[x]} cheats that save {x} steps") for x in savings if x >= 50]
print(f'To save at least {savethreshold} steps, there are {singlesavings} cheats')
