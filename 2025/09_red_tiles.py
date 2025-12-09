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