# %% part 1

def find_neighbors(grid,r,c):
    n = 0
    for x,y in dirs:
        if grid[r+x][c+y] in '@x':
            n += 1
    return n

# main
# lines = open('inputs/input_04_test.txt','r').read().splitlines()
lines = open('inputs/input_04.txt','r').read().splitlines()

# pad the lines with .
padstr = '.'*len(lines[0])
lines.insert(0,padstr)
lines.append(padstr)
for i in range(len(lines)):
    lines[i] = '.'+lines[i]+'.'
# _ = [print(x) for x in grid]

# breakout into grid
grid = [list(line) for line in lines]
# print(grid)
# _ = [print(''.join(x)) for x in grid]
# print()

# search for accessable paper rolls
dirs = (-1,-1,),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)
rows = len(grid)
cols = len(grid[0])
rolls = 0
for r in range(1,rows-1):
    for c in range(1,cols-1):
        if grid[r][c] == '@':
            if find_neighbors(grid,r,c) < 4:
                rolls += 1
                grid[r][c] = 'x'

# _ = [print(''.join(x)) for x in grid]
print(f'rolls = {rolls}')

# %% part 2

def find_neighbors(grid,r,c):
    n = 0
    for x,y in dirs:
        if grid[r+x][c+y] in '@x':
            n += 1
    return n

# main
# lines = open('inputs/input_04_test.txt','r').read().splitlines()
lines = open('inputs/input_04.txt','r').read().splitlines()

# pad the lines with .
padstr = '.'*len(lines[0])
lines.insert(0,padstr)
lines.append(padstr)
for i in range(len(lines)):
    lines[i] = '.'+lines[i]+'.'
# _ = [print(x) for x in grid]

# breakout into grid
grid = [list(line) for line in lines]
# print(grid)
# _ = [print(''.join(x)) for x in grid]
# print()

# search for accessable paper rolls
dirs = (-1,-1,),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)
rows = len(grid)
cols = len(grid[0])
rollslist = []
done = False
while not done:
    rolls = 0
    for r in range(1,rows-1):
        for c in range(1,cols-1):
            if grid[r][c] == '@':
                if find_neighbors(grid,r,c) < 4:
                    rolls += 1
                    grid[r][c] = '.'
    rollslist.append(rolls)
    # print(f'rolls = {rolls}, rollslist = {rollslist}')
    if rolls == 0:
        done = True

# _ = [print(''.join(x)) for x in grid]
print(f'total cleared rolls = {sum(rollslist)}')