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

# %% part 1
lines = open('inputs/input_09_test.txt','r').read().splitlines()
# lines = open('inputs/input_09.txt','r').read().splitlines()
'''
make a list of red tile coordinates
make a list of green tile coordinates
make a list of rectangles, sort by area
work thru the largest rectanges and test for all tiles
inside being red or green
'''
n = len(lines)
# list of reds
reds = [(0,0)]*n
for i,line in enumerate(lines):
    reds[i] = tuple([int(x) for x in line.split(',')])
print(reds)

# find areas, sort reverse
max_area = 0
areas = []
for a in range(n-1):
    for b in range(1,n):
        areas.append((abs(reds[a][0] - reds[b][0])+1)*\
        abs((reds[a][1] - reds[b][1])+1)),\
        (reds[a][0],reds[a][1]),(reds[b][0],reds[b][1])
areas.sort(reverse=True)
print(areas)

# list of greens (greens + reds)
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
print(greens)

# make a grid
x_values = [t[0] for t in reds]
y_values = [t[1] for t in reds]
xrange = (min(x_values),max(x_values))
yrange = (min(y_values),max(y_values))
print(xrange,yrange)
grid =[['.' for _ in range(xrange[1]+2)] for _ in range(yrange[1]+2)]
for red in reds:
    print(red[0],red[1])
    grid[red[1]][red[0]] = '#'
_ = [print(''.join(x)) for x in grid]

for green in greens:
    print(green[0],green[1])
    grid[green[1]][green[0]] = '#'
_ = [print(''.join(x)) for x in grid]
