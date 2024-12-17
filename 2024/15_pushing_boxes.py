# %%
# filestr = open('inputs/input_15_test.txt','r').read().split('\n\n')
filestr = open('inputs/input_15.txt','r').read().split('\n\n')

# %% part 1

def move_robot(grid, robot, dir):
    R,C = robot
    dr, dc = dirs[dir]
    # print(f'robot: {R,C}, dir: {dir}, {dr,dc}')
    n = 1
    if dr == 0:
        while grid[R][C+dc*n] == 'O':
            n += 1
        if grid[R][C+dc*n] == '.':
            for i in range(n,0,-1):
                grid[R][C+dc*i] = grid[R][C+dc*(i-1)]
            grid[R][C] = '.'
            robot = [R,C+dc]
    if dc == 0:
        while grid[R+dr*n][C] == 'O':
            n += 1
        if grid[R+dr*n][C] == '.':
            for i in range(n,0,-1):
                grid[R+dr*i][C] = grid[R+dr*(i-1)][C]
            grid[R][C] = '.'
            robot = [R+dr,C]
    return robot

def show_grid(grid):
    [print(''.join(x)) for x in grid]

# main
grid = filestr[0].splitlines()
grid = [list(x) for x in grid]
rows, cols = len(grid), len(grid[0])
instr = ''.join(filestr[1].splitlines())
# show_grid(grid)
# print(instr)

idx = filestr[0].find('@')
robot = [idx // (cols+1), idx % (cols+1)]
# print(robot, grid[robot[0]][robot[1]])
dirs = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)}

for dir in instr:
    # print(f'robot: {robot}, dir: {dir}')
    robot = move_robot(grid,robot,dir)
show_grid(grid)
print(f'robot = {robot}')

GPS = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'O':
            GPS += 100*r + c
print(f'GPS = {GPS}')

# %% part 2
def move_robot(grid, robot, dir):
    R,C = robot
    dr, dc = dirs[dir]
    # print(f'robot: {R,C}, dir: {dir}, {dr,dc}')
    n = 1
    if dr == 0:
        while grid[R][C+dc*n] in ['[',']']:
            n += 1
        if grid[R][C+dc*n] == '.':
            for i in range(n,0,-1):
                grid[R][C+dc*i] = grid[R][C+dc*(i-1)]
            grid[R][C] = '.'
            robot = [R,C+dc]
    if dc == 0:
        flags = []
        movers = [(R,C,'@')]
        flags = checkit(movers,flags,R,C,dr)
        if all(flags):
            # now lets move
            for r,c,V in movers:
                grid[r][c] = '.'
            for r,c,V in movers:
                grid[r+dr][c] = V
            robot = [R+dr,C]
    return robot

def checkit(movers,flags,r,c,dr):
    if grid[r+dr][c] == '#':
        flags.append(False)
        return flags
    if grid[r+dr][c] == '.':
        flags.append(True)
        return flags
    if grid[r+dr][c] == '[':
        movers.append((r+dr, c, grid[r+dr][c]))
        flags = checkit(movers, flags, r+dr, c, dr)
        movers.append((r+dr,c+1, grid[r+dr][c+1]))
        flags = checkit(movers, flags, r+dr, c+1, dr)
    if grid[r+dr][c] == ']':
        movers.append((r+dr, c-1, grid[r+dr][c-1]))
        flags = checkit(movers, flags, r+dr, c-1, dr)
        movers.append((r+dr, c, grid[r+dr][c]))
        flags = checkit(movers, flags, r+dr, c, dr)
    return flags

def expand_warehouse(grid):
    for r in range(rows):
        for c in range(cols):
            grid[r][c] = grid[r][c].replace('#','##')
            grid[r][c] = grid[r][c].replace('O','[]')
            grid[r][c] = grid[r][c].replace('.','..')
            grid[r][c] = grid[r][c].replace('@','@.')
        temp = [list(x) for x in ''.join(grid[r])]
        grid[r] = [''.join(x) for x in temp]
    # show_grid(grid)
    return grid

# main
grid = filestr[0].splitlines()
grid = [list(x) for x in grid]
rows, cols = len(grid), len(grid[0])
instr = ''.join(filestr[1].splitlines())
# print(instr)
grid = expand_warehouse(grid)
newfilestr = [''.join(x) for x in grid]
newfilestr = ''.join(newfilestr)
idx = newfilestr.find('@')
rows, cols = len(grid), len(grid[0])
robot = [idx // cols, idx % cols]
# print(robot, grid[robot[0]][robot[1]])
dirs = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)}

# show_grid(grid)
for dir in instr:
# for dir in ['<','^']:
    # print(f'robot: {robot}, dir: {dir}')
    robot = move_robot(grid,robot,dir)
# show_grid(grid)
print(f'robot = {robot}')

GPS = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '[':
            GPS += 100*r + c
print(f'GPS = {GPS}')
# %%
#  movers = set()
#         movers.add((R,C))
#         frontier = set()
#         tocheck = set()
#         tocheck.add((R+dr,C))
#         while tocheck:
#             r,c = tocheck.pop()
#             if grid[r][c] in ['[', ']', '.']:
#                 if grid[r][c] == '[':
#                     movers.append((r,c))
#                     movers.append((r,c+1))
#                     tocheck.add((r+dr,c))
#                     tocheck.add((r+dr,c+1))
#                 if grid[r][c] == ']':
#                     movers.append((r,c))
#                     movers.append((r,c+1))
#                     tocheck.add((r+dr,c))
#                     tocheck.add((r+dr,c+1))
#                 if grid[r][c] == '.':
#                     frontier.add((r,c))