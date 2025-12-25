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
print(f'{len(reds)} reds: {reds[:20]}')

# %%
# find areas, sort reverse
areas = []
for a in range(n-1):
    for b in range(1,n):
        areas.append((\
            abs(reds[a][0] - reds[b][0]+1)*abs(reds[a][1] - reds[b][1]+1),\
            (reds[a][0],reds[a][1]),(reds[b][0],reds[b][1]) ))
areas.sort(reverse=True)
print(f'{len(areas)} areas: {areas[:20]}')


# add in some greens to the polygon
# list of greens (greens + reds) make the border
greens = []
for i in range(n-1):
    if reds[i+1][0] == reds[i][0]:
        y = min(reds[i+1][1],reds[i][1])
        while y <= max(reds[i+1][1],reds[i][1]):
            greens.append((reds[i][0],y))
            y += 500
    else:
        x = min(reds[i+1][0],reds[i][0])
        while x <= max(reds[i+1][0],reds[i][0]):
            greens.append((x,reds[i][1]))
            x += 500
    greens.append(reds[i+1])
    # wrap around
# if reds[0][0] == reds[n-1][0]:
#     y = min(reds[0][1],reds[n-1][1])
#     while y <= max(reds[0][1],reds[n-1][1]):
#         greens.append((reds[n-1][0],y))
#         y += 100
# else:
#     x = min(reds[0][1],reds[n-1][1])
#     while x <= max(reds[0][0],reds[n-1][0]):
#         greens.append((x,reds[n-1][1]))
#         x += 100
print(f'{len(greens)} greens: {greens[:20]}')

# Build the list of all points
# Xs = [t[0] for t in reds]
# Ys = [t[1] for t in reds]
Xs = [t[0] for t in greens]
Ys = [t[1] for t in greens]
print(f'x range: {min(Xs),max(Xs)}, y range: {min(Ys),max(Ys)}')

# plot
# import matplotlib.pyplot as plt
# plt.plot(Xs,Ys,'x')
# plt.plot(Xs,Ys)


# loop thru rectangles, check for any greens inside
print(f'Looping thru {len(areas)} rectangles')
good_rect = False
cnt = 0
while not good_rect:
    good_rect = True
    # area, A, B = areas.pop(0)
    area, A, B = areas.pop(90000+7000)
    cnt += 1
    if cnt % 1000 == 0: # % 1000
        print(f'cnt = {cnt}, checking area {area, A, B} ')
    x_rect = (min(A[0],B[0]), max(A[0],B[0]))
    y_rect = (min(A[1],B[1]), max(A[1],B[1]))
    # find all relevent red points
    indx = [index for index, value in enumerate(Xs) if x_rect[0] < value < x_rect[1]]
    indy = [index for index, value in enumerate(Ys) if y_rect[0] < value < y_rect[1]]

    # print(f'                         x_rect = {x_rect}, y_rect = {y_rect}')
    # check that the reds are at least at the boundary of the rectangle
    # for indx1 in indx:
    #     if y_rect[0] < Ys[indx1] < y_rect[1]:
    #         good_rect = False
    # if good_rect == True:
    #     for indy1 in indy:
    #         if x_rect[0] < Xs[indy1] < x_rect[1]:
    #             good_rect = False
    # if cnt == 20000:
    #     good_rect = True


print(f'found {good_rect} cnt = {cnt}, area = {area}, A = {A}, B = {B}')
# plt.plot(Xs,Ys,'x',A[0],A[1],'ro',B[0],B[1],'r*')
plt.plot(Xs,Ys,A[0],A[1],'ro',B[0],B[1],'r*')

# 1666288864 is too high (used scale 1000)

# cnt = 90000, checking area 1716984150
# found area = 1666288864 (scale 100)

# cnt = 90000, checking area 1716984150
# found area = 1573323843 (too low. scale = 50, also 10)

# cnt = 90000+2499, found area = 1661338600 (too high
#  scale=50)



# %%
