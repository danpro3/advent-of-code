# %% part 1
# lines = open('inputs/input_09_test.txt','r').read().splitlines()
lines = open('inputs/input_09.txt','r').read().splitlines()

n = len(lines)
tiles = [(0,0)]*n
for i,line in enumerate(lines):
    tiles[i] = tuple([int(x) for x in line.split(',')])
print(tiles)

max_area = 0
for a in range(n-1):
    for b in range(1,n):
        area = (abs(tiles[a][0] - tiles[b][0])+1)*\
        abs((tiles[a][1] - tiles[b][1])+1)
        if area > max_area:
            max_area = area

print(f'max area = {max_area}')

# %% part 2
# lines = open('inputs/input_09_test.txt','r').read().splitlines()
lines = open('inputs/input_09.txt','r').read().splitlines()
'''
make a list of red tile coordinates
make a list of rectangles, sort by area
make a list of green tile coordinates
fill in the pattern
work thru the largest rectanges and test for all tiles
inside being red or green
'''
n = len(lines)
# list of reds
reds = [(0,0)]*n
for i,line in enumerate(lines):
    reds[i] = tuple([int(x) for x in line.split(',')])
print(reds[:20])
x_values = [t[0] for t in reds]
y_values = [t[1] for t in reds]
x_min = min(x_values)
y_min = min(y_values)
reds = [(x-x_min,y-y_min) for x,y in reds]
print(reds[:20])

# find areas, sort reverse
areas = []
for a in range(n-1):
    for b in range(1,n):
        areas.append((\
            abs(reds[a][0] - reds[b][0]+1)*abs(reds[a][1] - reds[b][1]+1),\
            (reds[a][0],reds[a][1]),(reds[b][0],reds[b][1]) ))
areas.sort(reverse=True)
print(areas[:20])

# list of greens (greens + reds) make the border
greens = set([])
for i in range(n-1):
    if reds[i+1][0] == reds[i][0]:
        y = min(reds[i+1][1],reds[i][1])
        while y <= max(reds[i+1][1],reds[i][1]):
            greens.add((reds[i][0],y))
            y += 1
    else:
        x = min(reds[i+1][0],reds[i][0])
        while x <= max(reds[i+1][0],reds[i][0]):
            greens.add((x,reds[i][1]))
            x += 1
    # wrap around
if reds[0][0] == reds[n-1][0]:
    y = min(reds[0][1],reds[n-1][1])
    while y <= max(reds[0][1],reds[n-1][1]):
        greens.add((reds[n-1][0],y))
        y += 1
else:
    x = min(reds[0][1],reds[n-1][1])
    while x <= max(reds[0][0],reds[n-1][0]):
        greens.add((x,reds[n-1][1]))
        x += 1
print(f'length of greens = {len(greens)}')

# make a grid
x_values = [t[0] for t in reds]
y_values = [t[1] for t in reds]
# xrange = (min(x_values),max(x_values))
# yrange = (min(y_values),max(y_values))
xrange = max(x_values)+1
yrange = max(y_values)+1
# print(xrange,yrange)
print('hello')
# grid =[['.' for _ in range(xrange[1]+2)] for _ in range(yrange[1]+2)]
grid = [['.']*(xrange+2)]
for _ in range(yrange+2):
    grid.append(['.']*(xrange+2))
# print(grid)

for red in reds:
    # print(red[0],red[1])
    grid[red[1]][red[0]] = '#'
# _ = [print(''.join(x)) for x in grid]
# print()
for green in greens:
    # print(green[0],green[1])
    grid[green[1]][green[0]] = '#'
_ = [print(''.join(x)) for x in grid]
print()

# fill in the grid
chars = ['.','#']
for r in range(len(grid)):
    # print(grid[r])
    n = 0
    for c in range(len(grid[r])):
        # print(r,c,grid[r][c],n)
        if grid[r][c] == '#' and grid[r][c+1:] == ['.']*len(grid[r][c+1:]):
            n = 0
            continue
        if grid[r][c] == '#' and grid[r][c+1] == '.' and n == 0:
            n = 1
        elif grid[r][c] == '#' and grid[r][c+1] == '.' and n == 1:
            n = 0
        elif grid[r][c] == '.' and n == 1:
            grid[r][c] = chars[n]
            greens.add((c,r))
# _ = [print(''.join(x)) for x in grid]
# print()
# print(areas)
# now loop thru rectangles and check for greens
found = False
rect = 0 # first rectangle with highest area
while not found:
    area, A, B = areas.pop(0)
    print(area,A,B)
    # build the list of points in the rectangle
    interior_points = []
    for x in range(min(A[0],B[0]), max(A[0],B[0])+1):
        for y in range(min(A[1],B[1]), max(A[1],B[1])+1):
            interior_points.append((x, y))
    # print(interior_points)
    
    # are all the points green?
    all_reds = True
    i = 0
    while all_reds and i < area:
        if interior_points[i] not in greens:
            all_reds = False
        i += 1
    # print(i)
    if all_reds == True:
        found = True
    
print(f'maximum area with all green/red tiles = {area}')
    


