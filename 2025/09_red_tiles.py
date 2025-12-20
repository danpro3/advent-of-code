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
work thru the largest rectanges and test for all tiles
inside being red or green
    Do this for each row (column): check min (max) green is less(greater) than
    the borders of the rectangle
'''
n = len(lines)
# list of reds
reds = [(0,0)]*n
for i,line in enumerate(lines):
    reds[i] = tuple([int(x) for x in line.split(',')])
print(f'Number of reds: {len(reds)}, reds: {reds[:20]}')


# find areas, sort reverse
areas = []
for a in range(n-1):
    for b in range(1,n):
        areas.append((\
            abs(reds[a][0] - reds[b][0]+1)*abs(reds[a][1] - reds[b][1]+1),\
            (reds[a][0],reds[a][1]),(reds[b][0],reds[b][1]) ))
areas.sort(reverse=True)
print(f'{len(areas)} areas: {areas[:20]}')

# scale down the red coords
x_values = [t[0] for t in reds]
y_values = [t[1] for t in reds]
# offset from zeros
x_min = min(x_values)
y_min = min(y_values)
# reds = [(x-x_min,y-y_min) for x,y in reds]
scale = 50# 100
reds = [(round((x-x_min)/scale)+1,round((y-y_min)/scale)+1) for x,y in reds]
x_values = [t[0] for t in reds]
y_values = [t[1] for t in reds]

print(f'{len(reds)} reds: {reds[:20]}')
print(f'x range: {min(x_values),max(x_values)}, y range: {min(y_values),max(y_values)}')
# print(f'x values: {x_values[:20]}')
# print(f'y values: {y_values[:20]}')

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
print(f'{len(greens)} greens: {greens}')

# better BFS get the coordinates of all tiles outside the loop
xrange = [0, max(x_values)+1]
yrange = [0, max(y_values)+1]
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
def move(todo):
    x,y = todo.pop(0)
    if (x,y) in visited:
        return
    else:
        visited.add((x,y))
        for dir in dirs:
            if x+dir[0] >= xrange[0] and x+dir[0] <= xrange[1]\
            and y+dir[1] >= yrange[0] and y+dir[1] <= yrange[1]\
            and (x+dir[0],y+dir[1]) not in greens:
                todo.append((x+dir[0],y+dir[1]))
            # and (x+dir[0] in x_values or y+dir[1] in y_values):

visited = set()
todo = [(0,0)]
while len(todo) > 0:
    # print(todo)
    move(todo)
print(f'length of visited = {len(visited)}')
# print(visited)

# ----  now loop thru rectangles
def rectangle_boundary_points(A, B):
    ABxmin, ABxmax = sorted([A[0], B[0]])
    ABymin, ABymax = sorted([A[1], B[1]])
    points = set()
    for x in range(ABxmin, ABxmax + 1):
        points.add((x, ABymin))
        points.add((x, ABymax))
    for y in range(ABymin, ABymax + 1):
        points.add((ABxmin, y))
        points.add((ABxmax, y))
    return sorted(points)

print(f'Looping thru {len(areas)} rectangles')
found = False
cnt = 0
# for _ in range(90000):
#     area, A, B = areas.pop(0)
while not found:
    area, A, B = areas.pop(90000)
    cnt += 1
    if cnt % 1000 == 0: 
        print(f'cnt = {cnt}, checking area {area}')
    A = (round((A[0]-x_min)/scale)+1,round((A[1]-y_min)/scale)+1)
    B = (round((B[0]-x_min)/scale)+1,round((B[1]-y_min)/scale)+1)
    points = rectangle_boundary_points(A, B)
    if set(points).intersection(visited):
        continue
    else:
        found = True
        
print(f'found area = {area}')
# 1666288864 is too high (used scale 1000)

# cnt = 90000, checking area 1716984150
# found area = 1666288864 (scale 100)

# cnt = 90000, checking area 1716984150
# found area = 1573323843 (too low. scale = 50, also 10)

# %%
# make a grid
grid = [['.']*(max(x_values)+2)]
for _ in range(max(y_values)+1):
    grid.append(['.']*(max(x_values)+2))
for green in greens:
    grid[green[1]][green[0]] = '#'
# for vis in visited:
#     grid[vis[1]][vis[0]] = 'x'
print(f'Grid complete: {len(grid)} x {len(grid[0])}')
_ = [print(''.join(x)) for x in grid]
print()



























# %%

# ----  now loop thru rectangles
print(f'Looping thru {len(areas)} rectangles')
found = False
cnt = 0
while found:
    cnt += 1
    area, A, B = areas.pop(0)
    # print(area,A,B)
    if cnt % 100 == 0: print(f'{cnt} area = {area,A,B}')
    # loop on the points in the rectangle
    x_min = min(A[0],B[0])
    x_max = max(A[0],B[0])
    y_min = min(A[1],B[1])
    y_max = max(A[1],B[1])

    this_rect = True

# %%
# better BFS get the coordinates of all tiles outside the loop

# range: 
x_values = [t[0] for t in reds]
y_values = [t[1] for t in reds]
xrange = (min(x_values)-1,max(x_values)+1)
yrange = (min(y_values)-1,max(y_values)+1)
print(f'x range: {xrange}, y range: {yrange}')
print(f'x values: {x_values[:20]}')
print(f'y values: {y_values[:20]}')

dirs = [(1,0),(0,1),(-1,0),(0,-1)]
def move(todo):
    x,y = todo.pop(0)
    if (x,y) in visited:
        return
    else:
        visited.add((x,y))
        for dir in dirs:
            if x+dir[0] >= xrange[0] and x+dir[0] <= xrange[1]\
            and y+dir[1] >= yrange[0] and y+dir[1] <= yrange[1]\
            and (x+dir[0],y+dir[1]) not in greens:
                todo.append((x+dir[0],y+dir[1]))
            # and (x+dir[0] in x_values or y+dir[1] in y_values):

visited = set()
todo = [(xrange[0],yrange[0])]
while len(todo) > 0:
    # print(todo)
    move(todo)
print(f'length of visited = {len(visited)}')
# print(visited)







# %% NOT USED

# now loop thru rectangles and check for edges
print(f'Looping thru {len(areas)} rectangles')
found = False
cnt = 0
while not found:
    cnt += 1
    area, A, B = areas.pop(0)
    # print(area,A,B)
    if cnt % 100 == 0: print(f'{cnt} area = {area,A,B}')
    # loop on the points in the rectangle
    x_min = min(A[0],B[0])
    x_max = max(A[0],B[0])
    y_min = min(A[1],B[1])
    y_max = max(A[1],B[1])
    this_rect = True
    
    wallpts = [(x_min,y) for y in range(y_min,y_max+1)] # wall 1
    # print(f'                 {len(wallpts)} wallpts 1: {wallpts[0:20]}')
    wallpts = set(wallpts) - set(greens)
    # print(f'                 {len(wallpts)} wallpts 1')
    # for x,y in wallpts:
    #     while this_rect and x > xrange[0]:
    #         if (x,y) in greens:
    #             x = xrange[0]-1 # set it outside the range
    #         x -= 1
    #     if x == xrange[0]:
    #         this_rect = False
    # if this_rect == False:
    #     continue

    wallpts = [(x_max,y) for y in range(y_min,y_max+1)] # wall 2
    # print(f'                 {len(wallpts)} wallpts 2: {wallpts[0:20]}')
    wallpts = set(wallpts) - set(greens)
    # print(f'                 {len(wallpts)} wallpts 2')
    # for x,y in wallpts:
    #     while this_rect and x < xrange[1]:
    #         if (x,y) in greens:
    #             x = xrange[1]+1 # set it outside the range
    #         x += 1
    #     if x == xrange[1]:
    #         this_rect = False
    # if this_rect == False:
    #     continue

    wallpts = [(x,y_min) for x in range(x_min,x_max+1)] # wall 3
    # print(f'                 {len(wallpts)} wallpts 3: {wallpts[0:20]}')
    wallpts = set(wallpts) - set(greens)
    # for x,y in wallpts:
    #     while this_rect and y > yrange[0]:
    #         if (x,y) in greens:
    #             y = yrange[0]-1 # set it outside the range
    #         y -= 1
    #     if y == yrange[0]:
    #         this_rect = False
    # if this_rect == False:
    #     continue

    wallpts = [(x,y_max) for x in range(x_min,x_max+1)] # wall 4
    # print(f'                 {len(wallpts)} wallpts 4: {wallpts[0:20]}')
    wallpts = set(wallpts) - set(greens)
    # for x,y in wallpts:
    #     while this_rect and y < yrange[1]:
    #         if (x,y) in greens:
    #              y = yrange[1]+1 # set it outside the range
    #         y += 1
    #     if y == yrange[1]:
    #         this_rect = False

    # if this_rect: # still true after all wall checks
    #     found = True

# finish 
print(f'maximum area with all green/red tiles = {area} coords: {A, B}')
    
# %% NOT USED

# BFS: get the coordinates of all tiles outside the loop
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
def move(todo):
    r,c = todo.pop(0)
    # if (r,c) in visited:
    #     return
    # else:
    # visited.add((r,c))
    for dir in dirs:
        if r+dir[0] >= xrange[0] and r+dir[0] <= xrange[1]\
        and c+dir[1] >= yrange[0] and c+dir[1] <= yrange[1]\
        and (r+dir[0],c+dir[1]) not in greens\
        and (r,c) not in visited:
            todo.append((r+dir[0],c+dir[1]))
    visited.add((r,c))

visited = set()
todo = [(xrange[0],yrange[0])]
while len(todo) > 0:
    # print(todo)
    move(todo)
print(f'length of visited = {len(visited)}')

# now loop thru rectangles and check for greens
print('Looping thru rectangles')
found = False
while not found:
    area, A, B = areas.pop(0)
    # print(area,A,B)
    # loop on the points in the rectangle
    x = min(A[0],B[0])
    x_max = max(A[0],B[0])
    this_rect = True
    while this_rect and x <= x_max:
        y = min(A[1],B[1])
        y_max = max(A[1],B[1])
        while this_rect and y <= y_max:
            if (x,y) in visited:
                this_rect = False
            y += 1
        x += 1
    if this_rect == True:
        found = True
# finish 
print(f'maximum area with all green/red tiles = {area} coords: {A, B}')

# %% NOT USED

# make a grid
grid = [['.']*(xrange[1]+1)]
for _ in range(yrange[1]):
    grid.append(['.']*(xrange[1]+1))
for green in greens:
    grid[green[1]][green[0]] = '#'
for vis in visited:
    grid[vis[1]][vis[0]] = 'x'
print(f'Grid complete: {len(grid)} x {len(grid[0])}')
_ = [print(''.join(x)) for x in grid]
print()




# %%
# Very useful but NOT USED

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
grid = [['.']*(xrange+1)]
for _ in range(yrange):
    grid.append(['.']*(xrange+1))
print(f'Grid complete:      {len(grid)} x {len(grid[0])}')
print(f'size of grid      = {len(grid)*len(grid[0])}')
print(f'length of greens  = {len(greens)}')
print(f'length of visited = {len(visited)}')

for tile in greens:
    grid[tile[1]][tile[0]] = '#'

# for green in greens:
#     grid[green[1]][green[0]] = '#'
    # print(green[0],green[1])
_ = [print(''.join(x)) for x in grid]
print()



# %%


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


# now loop thru rectangles and check for greens
this_rect = True
while this_rect:
    area, A, B = areas.pop(0)
    print(area,A,B)
    # loop on the points in the rectangle
    x = min(A[0],B[0])
    x_max = max(A[0],B[0])
    while this_rect and x <= x_max:
        y = min(A[1],B[1])
        y_max = max(A[1],B[1])
        while this_rect and y <= y_max:
            if grid[x][y] == '.':
                this_rect = False
            y += 1
        x += 1
# %%
