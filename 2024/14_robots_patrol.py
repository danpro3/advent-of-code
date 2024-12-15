# %%
import re
import numpy as np
# lines = open('inputs/input_14_test.txt','r').read().splitlines()
# rows = 7; cols = 11 # example, given
lines = open('inputs/input_14.txt','r').read().splitlines()
rows = 103; cols = 101 # example, given
grid = [['.' for _ in range(cols)] for _ in range(rows)]
# _ = [print(''.join(x)) for x in grid]
# print(grid)
# print(lines)

# %% part 1

def show_grid(robots):
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    # print(robots)
    for r,c,vr,vc in robots:
        # print(r,c)
        if grid[r][c].isnumeric():
            grid[r][c] = str(int(grid[r][c]) + 1)
        else:
            grid[r][c] = '1'
    _ = [print(''.join(x)) for x in grid]
    return

def move_robots(robots):
    for i, robot in enumerate(robots):
        r,c,vr,vc = robot
        r += vr
        c += vc
        if r >= rows:
            r = r % rows
        if r < 0:
            r = rows - abs(r) % rows
        if c >= cols:
            c = c % cols
        if c < 0:
            c = cols - abs(c) % cols
        robots[i] = [r,c,vr,vc]
    return robots

def quad_count(robots):
    Q = [0,0,0,0]
    for r,c,vr,vc in robots:
        if r < rows // 2 and c < cols // 2:
            Q[0] += 1
        if r < rows // 2 and c > cols // 2:
            Q[1] += 1
        if r > rows // 2 and c < cols // 2:
            Q[2] += 1
        if r > rows // 2 and c > cols // 2:
            Q[3] += 1
    return Q

# main
robots = []
for i, line in enumerate(lines):
    Q = [int(x) for x in re.findall('(-\d+|\d+)',line)]
    robots.append([Q[1], Q[0], Q[3], Q[2]])

for t in range(1,101):
    move_robots(robots)
    # [print(x) for x in robots]
# show_grid(robots)
# print(robots)
quads = quad_count(robots)
print(quads)
print(f'safety factor = {np.prod(quads)}')


# %% part 2

def build_grid(robots):
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    # print(robots)
    for r,c,vr,vc in robots:
        grid[r][c] = '#'
    return(grid)

# main
robots = []
for i, line in enumerate(lines):
    Q = [int(x) for x in re.findall('(-\d+|\d+)',line)]
    robots.append([Q[1], Q[0], Q[3], Q[2]])

moves = 0
found = False
while found == False:
    print(f'moves = {moves}') if moves % 100 == 0 else 0
    moves += 1
    move_robots(robots)
    grid = build_grid(robots)
    bigstrings = []
    for i in range(len(grid[0])):
        bigstrings = [''.join(x) for x in grid]

        for bigstring in bigstrings:
            foundsomething = re.findall('###########',bigstring)
            if foundsomething != []:
                found = True

show_grid(robots)
print(f'total moves = {moves}')
