# %%
# filestr = open('inputs/input_16_test.txt','r').read()
filestr = open('inputs/input_16_test2.txt','r').read()
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
    if (r, c, dir) in visited:
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
heappush(todo,(0, S[0], S[1],'R'))
print(todo)

while(todo):
    score, todo = move(todo)
    # print(f'score = {score}, length todo = {len(todo)}')

print(f'best score = {score}')

# %%

def move2(todo):
    score , r, c, dir, tiles = heappop(todo)
    if (r, c, dir) in visited:
        return tiles, score, todo
    else:
        visited.add((r,c,dir))
    # print(f'grid [{r}][{c}] = {grid[r][c]}')
    if grid[r][c] == 'E':
        print(f'Done. r,c = {r,c}, score = {score}, tiles = {len(tiles)}')
        todo = []
        return tiles, score, todo
    mylist = list(tiles)
    if dir == 'U':
        if grid[r-1][c] in ['.','E']:
            mylist.append((r-1,c))
            heappush(todo, (score+1+0000, r-1, c, 'U',tuple(mylist)))
        if grid[r][c+1] in ['.','E']:
            mylist.append((r,c+1))
            heappush(todo, (score+1+1000, r, c+1, 'R',tuple(mylist)))
        if grid[r+1][c] in ['.','E']:
            mylist.append((r+1,c))
            heappush(todo, (score+1+2000, r+1, c, 'D',tuple(mylist)))
        if grid[r][c-1] in ['.','E']:
            mylist.append((r,c-1))
            heappush(todo, (score+1+1000, r, c-1, 'L',tuple(mylist)))
    if dir == 'R':
        if grid[r-1][c] in ['.','E']:
            mylist.append((r-1,c))
            heappush(todo, (score+1+1000, r-1, c, 'U',tuple(mylist)))
        if grid[r][c+1] in ['.','E']:
            mylist.append((r,c+1))
            heappush(todo, (score+1+0000, r, c+1, 'R',tuple(mylist)))
        if grid[r+1][c] in ['.','E']:
            mylist.append((r+1,c))
            heappush(todo, (score+1+1000, r+1, c, 'D',tuple(mylist)))
        if grid[r][c-1] in ['.','E']:
            mylist.append((r,c-1))
            heappush(todo, (score+1+2000, r, c-1, 'L',tuple(mylist)))
    if dir == 'D':
        if grid[r-1][c] in ['.','E']:
            mylist.append((r-1,c))
            heappush(todo, (score+1+2000, r-1, c, 'U',tuple(mylist)))
        if grid[r][c+1] in ['.','E']:
            mylist.append((r,c+1))
            heappush(todo, (score+1+1000, r, c+1, 'R',tuple(mylist)))
        if grid[r+1][c] in ['.','E']:
            mylist.append((r+1,c))
            heappush(todo, (score+1+0000, r+1, c, 'D',tuple(mylist)))
        if grid[r][c-1] in ['.','E']:
            mylist.append((r,c-1))
            heappush(todo, (score+1+1000, r, c-1, 'L',tuple(mylist)))
    if dir == 'L':
        if grid[r-1][c] in ['.','E']:
            mylist.append((r-1,c))
            heappush(todo, (score+1+1000, r-1, c, 'U',tuple(mylist)))
        if grid[r][c+1] in ['.','E']:
            mylist.append((r,c+1))
            heappush(todo, (score+1+2000, r, c+1, 'R',tuple(mylist)))
        if grid[r+1][c] in ['.','E']:
            mylist.append((r+1,c))
            heappush(todo, (score+1+1000, r+1, c, 'D',tuple(mylist)))
        if grid[r][c-1] in ['.','E']:
            mylist.append((r,c-1))
            heappush(todo, (score+1+0000, r, c-1, 'L',tuple(mylist)))
    return tiles, score, todo

todo = []
visited = set()
goodseats = set()

# best_score = 7036
heappush(todo,(0, S[0], S[1],'R', ()))
print(todo)

while(todo):
    if grid[todo[0][1]][todo[0][2]] == 'E':
        print(f'length of tiles = {len(tiles)}')
    if goodseats == []:
        goodseats = todo[0][4]
    else:
        goodseats = goodseats.union(todo[0][4])
    tiles, score, todo = move2(todo)
    # print(f'score = {score}, length todo = {len(todo)}')

# have to add one for starttiles
print(f'best score = {score}, tiles = {len(tiles)+1}') 
print(f'number of good seats = {len(goodseats)}')