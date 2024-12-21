# %% part 1
# lines = open('inputs/input_18_test.txt','r').read().splitlines()
lines = open('inputs/input_18.txt','r').read().splitlines()
# rows = 7; startbits = 12
rows = 71; startbits = 2024 # full input
grid = [['.']*rows for _ in range(rows)]

for line in lines[0:startbits]:
    a = line.split(',')
    grid[int(a[1])][int(a[0])] = '#'
_=[print(''.join(x)) for x in grid]

# %% ----------------------------------------
from heapq import heapify, heappush, heappop
def move(todo):
    steps, r, c = heappop(todo)
    if (r,c) == END:
        # print(f'done. steps = {steps}')
        todo = []
        return todo
    if (r,c) in cache:
        return todo
    else:
        cache.add((r,c))
    for dr, dc in dirs:
        if 0 <= r+dr < rows and 0 <= c+dc < rows:
            if grid[r+dr][c+dc] == '.':
                todo.append((steps+1, r+dr, c+dc))
    return todo

# main -------
START = (0,0)
END = (rows-1,rows-1)
dirs = [(-1,0), (0,1), (1,0), (0,-1)]
cache = set()
todo = [(0, START[0], START[1])]
while todo:
    # print(f'todo: {todo}')
    steps, r, c = todo[0]
    todo = move(todo)

print(f'best path steps = {steps}')


# %% part 2

# main -------
START = (0,0)
END = (rows-1,rows-1)
dirs = [(-1,0), (0,1), (1,0), (0,-1)]

# drop bits until can't find a path to the end
grid = [['.']*rows for _ in range(rows)]
for line in lines[0:startbits]:
    a = line.split(',')
    grid[int(a[1])][int(a[0])] = '#'
stillgood = True
i = startbits-1
while stillgood:
    # print(f'i: {i}')
    a = lines[i].split(',')
    grid[int(a[1])][int(a[0])] = '#'
    cache = set()
    todo = [(0, START[0], START[1])]
    while todo:
        # print(f'todo: {todo}')
        steps, r, c = todo[0]
        todo = move(todo)
    if (r,c) != END:
        print(f'blocked by x,y {int(a[0]), int(a[1])}. bits fallen = {i+1} r,c = {(r,c)}')
        stillgood = False
    i += 1

# print(f'best path steps = {steps}')