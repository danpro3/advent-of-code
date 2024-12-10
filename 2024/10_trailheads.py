# %% 
# load input
import re
filestr = open('inputs/input_10_test.txt','r').read()
# filestr = open('inputs/input_10.txt','r').read()
# filestr = open('inputs/input_06_test.txt','r').read()
grid = filestr.splitlines()
# startidx = filestr.index('^')
# start = [startidx//rows-1, startidx % (cols+1)]
# print(f'startidx = {startidx}, start = {start}')
_=[print(x) for x in grid]
# %%
# main
from heapq import heapify, heappush, heappop
rows = len(grid)
cols = len(grid[0])

def find_trailheads():
    res = [x for x in re.finditer('0',filestr)]
    locs = [match.span()[0] for match in res]
    # print(locs)
    trailheads = []
    for loc in locs:
        trailheads.append((loc//(cols+1), loc%(cols+1)))
    print(trailheads)
    return trailheads

# def find_hikes(loc):
#     move = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
    
#     todo = []
#     if 

#     while todo:

def V(r,c): # return the value of the grid
    return grid[r][c]

def move(todo):
    dist, r, c, dir = heappop(todo)
    # if we've been here before, end this thread
    key = (r, c, dir)
    # if key in cache:
    #     # print(r,c,dir,'in cache')
    #     return todo
    # else:
    #     # add this state to the cache
    #     cache[key] = 0
    #     cache_grid[r][c] = '#'

    if grid[r][c] == '9':  # found one!
        score.append(1)
        return todo
    # check up
    if r>0 and V(r-1,c) < V(r,c)+1:
        heappush(todo, (dist+1, r-1, c, 'U'))
    # check down
    if r<rows-1 and V(r+1,c) < V(r,c)+1:
        heappush(todo, (dist+1, r+1, c, 'D'))
    # check left
    if c>0 and V(r,c-1) < V(r,c)+1:
        heappush(todo, (dist+1, r, c-1, 'L'))
    # check right
    if c<cols-1 and V(r,c+1) < V(r,c)+1:
        heappush(todo, (dist+1, r, c+1, 'R'))
    return(todo)


# main
trailheads = find_trailheads()
for trailhead in trailheads:
    score = [] # tally up how many hikes

    # start
    r,c = trailhead
    # cache = {}   # list of all places been: (row, col, dir)
    # todo = start_the_todo(S)
    todo = []
    # heapify(todo)
    heappush(todo, (-1, r, c, ''))

    print(todo)
    while len(todo) > 0:# and todo[0][1:3] != E:
        # print(todo[0][1:3])
        # print(todo)
        todo = move(todo)
        # print(f'dist = {todo[0][0]}')








