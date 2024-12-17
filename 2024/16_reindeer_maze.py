# %%
filestr = open('inputs/input_16_test.txt','r').read()
# filestr = open('inputs/input_16.txt','r').read()
grid = filestr.splitlines()
rows = len(grid)
cols = len(grid[0])
idx = filestr.index('S')
S = [idx//(cols+1), idx % (cols+1)]
idx = filestr.index('E')
E = [idx//(cols+1), idx % (cols+1)]
print(f'start = {S}, end = {E}')
_=[print(x) for x in grid]
# %% Part 1
from heapq import heapify, heappush, heappop

def move(todo):
    score , r, c, dir = heappop(todo)
    if (r, c, dir) in visited or score > best_score:
        return score, todo
    else:
        visited.add((r,c,dir))
    # print(f'grid [{r}][{c}] = {grid[r][c]}')
    if grid[r][c] == 'E':
        print(f'Done. r,c = {r,c}, score = {score}')
        todo = []
        return score, todo
    if dir == 'U':
        if grid[r-1][c] in ['.','E']:
            heappush(todo, (score+1+0000, r-1, c, 'U'))
        if grid[r][c+1] in ['.','E']:
            heappush(todo, (score+1+1000, r, c+1, 'R'))
        if grid[r+1][c] in ['.','E']:
            heappush(todo, (score+1+2000, r+1, c, 'D'))
        if grid[r][c-1] in ['.','E']:
            heappush(todo, (score+1+1000, r, c-1, 'L'))
    if dir == 'R':
        if grid[r-1][c] in ['.','E']:
            heappush(todo, (score+1+1000, r-1, c, 'U'))
        if grid[r][c+1] in ['.','E']:
            heappush(todo, (score+1+0000, r, c+1, 'R'))
        if grid[r+1][c] in ['.','E']:
            heappush(todo, (score+1+1000, r+1, c, 'D'))
        if grid[r][c-1] in ['.','E']:
            heappush(todo, (score+1+2000, r, c-1, 'L'))
    if dir == 'D':
        if grid[r-1][c] in ['.','E']:
            heappush(todo, (score+1+2000, r-1, c, 'U'))
        if grid[r][c+1] in ['.','E']:
            heappush(todo, (score+1+1000, r, c+1, 'R'))
        if grid[r+1][c] in ['.','E']:
            heappush(todo, (score+1+0000, r+1, c, 'D'))
        if grid[r][c-1] in ['.','E']:
            heappush(todo, (score+1+1000, r, c-1, 'L'))
    if dir == 'L':
        if grid[r-1][c] in ['.','E']:
            heappush(todo, (score+1+1000, r-1, c, 'U'))
        if grid[r][c+1] in ['.','E']:
            heappush(todo, (score+1+2000, r, c+1, 'R'))
        if grid[r+1][c] in ['.','E']:
            heappush(todo, (score+1+1000, r+1, c, 'D'))
        if grid[r][c-1] in ['.','E']:
            heappush(todo, (score+1+0000, r, c-1, 'L'))
    return score, todo

todo = []
visited = set()
best_score = 7036
heappush(todo,(0, S[0], S[1],'R'))
print(todo)

while(todo):
    score, todo = move(todo)
    # print(f'score = {score}, length todo = {len(todo)}')

print(f'best score = {score}')

# %%

def move2(todo):
    score , r, c, dir, tiles = heappop(todo)
    if (r, c, dir, tiles) in visited or score > best_score:
        return tiles, score, todo
    else:
        visited.add((r,c,dir,tiles))
    # print(f'grid [{r}][{c}] = {grid[r][c]}')
    if grid[r][c] == 'E':
        print(f'Done. r,c = {r,c}, score = {score}, tiles = {tiles}')
        # todo = []
        return tiles, score, todo
    if dir == 'U':
        if grid[r-1][c] in ['.','E']:
            heappush(todo, (score+1+0000, r-1, c, 'U',tuple(list(tiles).append((r-1,c)))))
        if grid[r][c+1] in ['.','E']:
            heappush(todo, (score+1+1000, r, c+1, 'R',tuple(list(tiles).append((r,c+1)))))
        if grid[r+1][c] in ['.','E']:
            heappush(todo, (score+1+2000, r+1, c, 'D',tuple(list(tiles).append((r+1,c)))))
        if grid[r][c-1] in ['.','E']:
            heappush(todo, (score+1+1000, r, c-1, 'L',tuple(list(tiles).append((r,c-1)))))
    print(f'tiles = {tiles}')
    if dir == 'R':
        if grid[r-1][c] in ['.','E']:
            heappush(todo, (score+1+1000, r-1, c, 'U',tuple(list(tiles).append((r-1,c)))))
        if grid[r][c+1] in ['.','E']:
            heappush(todo, (score+1+0000, r, c+1, 'R',tuple(list(tiles).append((r,c+1)))))
        if grid[r+1][c] in ['.','E']:
            heappush(todo, (score+1+1000, r+1, c, 'D',tuple(list(tiles).append((r+1,c)))))
        if grid[r][c-1] in ['.','E']:
            heappush(todo, (score+1+2000, r, c-1, 'L',tuple(list(tiles).append((r,c-1)))))
    if dir == 'D':
        if grid[r-1][c] in ['.','E']:
            heappush(todo, (score+1+2000, r-1, c, 'U',tuple(list(tiles).append((r-1,c)))))
        if grid[r][c+1] in ['.','E']:
            heappush(todo, (score+1+1000, r, c+1, 'R',tuple(list(tiles).append((r,c+1)))))
        if grid[r+1][c] in ['.','E']:
            heappush(todo, (score+1+0000, r+1, c, 'D',tuple(list(tiles).append((r+1,c)))))
        if grid[r][c-1] in ['.','E']:
            heappush(todo, (score+1+1000, r, c-1, 'L',tuple(list(tiles).append((r,c-1)))))
    if dir == 'L':
        if grid[r-1][c] in ['.','E']:
            heappush(todo, (score+1+1000, r-1, c, 'U',tuple(list(tiles).append((r-1,c)))))
        if grid[r][c+1] in ['.','E']:
            heappush(todo, (score+1+2000, r, c+1, 'R',tuple(list(tiles).append((r,c+1)))))
        if grid[r+1][c] in ['.','E']:
            heappush(todo, (score+1+1000, r+1, c, 'D',tuple(list(tiles).append((r+1,c)))))
        if grid[r][c-1] in ['.','E']:
            heappush(todo, (score+1+0000, r, c-1, 'L',tuple(list(tiles).append((r,c-1)))))
    return tiles, score, todo

todo = []
visited = set()
best_score = 7036
heappush(todo,(0, S[0], S[1],'R', ((S[0], S[1]))))
print(todo)

while(todo):
    tiles, score, todo = move2(todo)
    # print(f'score = {score}, length todo = {len(todo)}')

print(f'best score = {score}, tiles = {tiles}')