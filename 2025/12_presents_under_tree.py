# %% part 1
import matplotlib.pylab as plt
lines = open('inputs/input_12_test.txt','r').read().split('\n\n')
# lines = open('inputs/input_12.txt','r').read().split('\n\n')
print(f"number of lines = {len(lines)}")
# print(lines)

P = {} # dictionary of presents
for i,line in enumerate(lines[:6]):
    piece = int(lines[i][0])
    P[piece] = []
    y = 2
    for L,mystr in enumerate(line.split('\n')[1:]):
        # print(mystr)
        for x in range(3):
            if mystr[x] == '#':
                P[piece].append((x,y))
        y -= 1
for key, value in P.items():
    print(f"{key}: {value}")

trees = [] # list of trees with grid size and list of required presents
for line in lines[6].split('\n'):
    # print(line.split(' ')[0][:-1])
    tree = {}
    tree['XY'] = [int(x) for x in line.split(' ')[0][:-1].split('x')]
    tree['piece_list'] = [int(x) for x in line.split(' ')[1:]]
    trees.append(tree)
_ = [print(x) for x in trees]

def print_grid(coords):
    Xs,Ys = map(list, zip(*coords))
    ax.xaxis.get_major_locator().set_params(integer=True)
    ax.yaxis.get_major_locator().set_params(integer=True)
    plt.plot(Xs,Ys,'s')
    return

def move(piece, dir): # piece = list of coords, dir = (-1,0), ...
    return [(x+dir[0], y+dir[1]) for (x,y) in piece]

def flip(piece,f): # piece = list of coords, flip horizontally, f = 0,1
    if f == 1:
        return [(2-x, y) for (x,y) in piece]
    else:
        return piece

def rot(piece,dir): # dir = +1 for CCW, -1 for CW
    CCW = {(0,0):(2,0), (1,0):(2,1), (2,0):(2,2),\
           (0,1):(1,0), (1,1):(1,1), (2,1):(1,2),\
           (0,2):(0,0), (1,2):(0,1), (2,2):(0,2)}
    new_piece = piece.copy()
    for r in range(dir):
        for i,xy in enumerate(new_piece):
            new_piece[i] = CCW[xy]
    return new_piece

# %% main
def BFS(piece_pile):
    visited = set()
    todo = []
    layout = set()
    cnt = 0
    this_piece = P[piece_pile[cnt]]
    # add the first piece, all orientations with an empty layout
    for dx in range(Xlim-2):
        for dy in range(Ylim-2):
            # every flip
            for f in range(2):
                # every rotaion
                for r in range(4):
                    new_piece = flip(this_piece,f)
                    new_piece = rot(new_piece,r)
                    new_piece = move(new_piece,(dx,dy))
                    todo.append((layout, cnt, new_piece))

    while todo:
        # _=[print(x) for x in todo]
        layout, cnt, this_piece = todo.pop(-1)
        # print(f'    pop. len layout: {len(layout)}')
        # check for fit
        if (tuple(layout), cnt, tuple(this_piece)) in visited:
            continue
        else:
            visited.add((tuple(layout), cnt, tuple(this_piece)))           
        if any(coord in layout for coord in this_piece):
            continue

        # check for done
        if cnt == len(piece_pile)-1 and not any(coord in layout for coord in this_piece):
            return layout.union(this_piece), cnt+1, True
        
        # print(f'len todo: {len(todo)}, current cnt: {cnt}')
        # place it and add the new piece
        for dx in range(Xlim-2):
            for dy in range(Ylim-2):
                # every rotaion
                for r in range(4):
                    # every flip
                    for f in range(2):
                        new_piece = flip(P[piece_pile[cnt+1]],f)
                        new_piece = rot(new_piece,r)
                        new_piece = move(new_piece,(dx,dy))
                        todo.append((layout.union(this_piece),cnt+1,new_piece))
    return layout, cnt, False


for tree in [trees[1]]:
    print(tree)
    Xlim = tree['XY'][0]
    Ylim = tree['XY'][1]
    piece_pile = []
    for i,n_pieces in enumerate(tree['piece_list']):
        for cnt in range(n_pieces):
            piece_pile.append(i)
    piece_pile = piece_pile[::-1]
    # piece_pile = [0,0,0]
    print(f'piece list: {tree["piece_list"]}, piece_pile: {piece_pile}')
    layout, cnt, can_fit = BFS(piece_pile)
    print(f'len layout: {len(layout)}, cnt: {cnt}, can fit: {can_fit}')

 
    ax = plt.figure().gca()
    print_grid(layout)
    plt.xlim(-.3,Xlim-1+.3)
    plt.ylim(-.3,Ylim-1+.3)
    ax.set_aspect('equal')
    plt.show()

    