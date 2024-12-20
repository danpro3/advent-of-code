# %% part 1
# lines = open('inputs/input_18_test.txt','r').read().splitlines()
lines = open('inputs/input_18.txt','r').read().splitlines()
# rows = 7
rows = 71 # full input
grid = [['.']*rows for _ in range(rows)]

for line in lines[0:1024]:
    a = line.split(',')
    grid[int(a[1])][int(a[0])] = '#'
_=[print(''.join(x)) for x in grid]

# %% ----------------------------------------
from heapq import heapify, heappush, heappop
def move(todo):
    steps, r, c = heappop(todo)
    if (r,c) == END:
        print(f'done. steps = {steps}')
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


# %%
print(cache)
print(E)