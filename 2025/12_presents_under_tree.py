# %% part 1
lines = open('inputs/input_12_test.txt','r').read().split('\n\n')
# lines = open('inputs/input_12.txt','r').read().split('\n\n')
print(f"number of lines = {len(lines)}")
# print(lines)

P = {} # dictionary of presents
for i,line in enumerate(lines[:6]):
    piece = int(lines[i][0])
    P[piece] = []
    y = 0
    for L,mystr in enumerate(line.split('\n')[1:]):
        # print(mystr)
        for x in range(3):
            if mystr[x] == '#':
                P[piece].append((x,y))
        y += 1
for key, value in P.items():
    print(f"{key}: {value}")

trees = [] # list of trees with grid size and list of required presents
for line in lines[6].split('\n'):
    # print(line.split(' ')[0][:-1])
    tree = {}
    tree['XY'] = [int(x) for x in line.split(' ')[0][:-1].split('x')]
    tree['pres'] = [int(x) for x in line.split(' ')[1:]]
    trees.append(tree)
_ = [print(x) for x in trees]

# %% 
import matplotlib.pylab as plt
    


def print_grid(coords):
    Xs,Ys = map(list, zip(*coords))
    ax.xaxis.get_major_locator().set_params(integer=True)
    ax.yaxis.get_major_locator().set_params(integer=True)
    plt.plot(Xs,Ys,'s')
    return


def move(piece, dir): # piece = list of coords, dir = (-1,0), ...
    return


def rot(piece,dir): # dir = +1 for CCW, -1 for CW
    CCW = {(0,0):(2,0), (1,0):(2,1), (2,0):(2,2),\
           (0,1):(1,0), (1,1):(1,1), (2,1):(1,2),\
           (0,2):(0,0), (1,2):(0,1), (2,2):(0,2)}
    CW = dict((v,k) for k,v in CCW.items())
    new_piece = piece.copy()
    for r in range(dir):
        for i,xy in enumerate(new_piece):
            new_piece[i] = CCW[xy]
    for r in range(-dir):
        for i,xy in enumerate(new_piece):
            new_piece[i] = CW[xy]
    return new_piece



def BFS(tree):
    1
    return True


for tree in [trees[0]]:
    print(P[0])
    print()
    p2 = rot(P[0],1)
    p2 = rot(p2,-1)
    print(p2)
    # fit = BFS(tree)
    # print(fit)
    # print_grid(P[0])
    print()

    ax = plt.figure().gca()
    print_grid([(tree['XY'][0], tree['XY'][1])])
    print_grid(rot(P[1],-3))
    plt.show()

    