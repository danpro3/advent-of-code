# %% 
# load input
import re
filestr = '89010123\n78121874\n87430965\n96549874\n45678903\n32019012\n01329801\n10456732'
# filestr = open('inputs/input_10_test.txt','r').read()
# filestr = open('inputs/input_10.txt','r').read()
# filestr = open('inputs/input_06_test.txt','r').read()
grid = filestr.splitlines()
# startidx = filestr.index('^')
# start = [startidx//rows-1, startidx % (cols+1)]
# print(f'startidx = {startidx}, start = {start}')
_=[print(x) for x in grid]
# %%
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

def find_hikes(trailhead):
    # move = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
    r,c = trailhead
    score = []
    todo = []
    heappush(todo, (-1, r, c)
    while todo:
        move(todo)
    return score

def V(r,c): # return the value of the grid
    return grid[r][c]

def move(todo):
    dist, r, c = heappop(todo)
    if grid[r][c] == '9':  # found one!
        score.append(1)
        return todo
    # check up
    if r>0 and V(r-1,c) < V(r,c)+1:
        heappush(todo, (dist+1, r-1, c)
    # check down
    if r<rows-1 and V(r+1,c) < V(r,c)+1:
        heappush(todo, (dist+1, r+1, c)
    # check left
    if c>0 and V(r,c-1) < V(r,c)+1:
        heappush(todo, (dist+1, r, c-1)
    # check right
    if c<cols-1 and V(r,c+1) < V(r,c)+1:
        heappush(todo, (dist+1, r, c+1)
    return(todo)

# main
trailheads = find_trailheads()
total_score = 0
for trailhead in trailheads:
    r,c = trailhead
    score = find_hikes(trailhead)
    total_score = += score
print(f'total score = {total_score}')







