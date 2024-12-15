# %%
filestr = open('inputs/input_15_test.txt','r').read().split('\n\n')
# lines = open('inputs/input_14.txt','r').read().splitlines()

# %%

def move_robot(grid, robot, dir):
    R,C = robot
    dr, dc = dirs[dir]
    if dr == 0:
        while grid[R][C+dc] not in ['.','#']:
            1

    return grid

def calc_GPS(grid):
    GPS = 1
    return GPS


# main
grid = filestr[0].splitlines()
rows, cols = len(grid), len(grid[0])
instr = ''.join(filestr[1].splitlines())
_ = [print(x) for x in grid]
print(instr)

idx = filestr[0].find('@')
robot = [idx // (cols+1), idx % (cols+1)]
print(robot, grid[robot[0]][robot[1]])
dirs = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)}

for dir in instr:
    move_robot(grid,robot,dir)

GPS = calc_GPS(grid)
print(f'GPS = {GPS}')
