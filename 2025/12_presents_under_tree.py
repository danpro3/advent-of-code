# %% part 1
import matplotlib.pylab as plt
lines = open('inputs/input_12_test.txt','r').read().split('\n\n')
# lines = open('inputs/input_12.txt','r').read().split('\n\n')
print(f"number of lines = {len(lines)}")
# print(lines)

P: dict[int,set[tuple[int, int]]] = {} # dictionary of presents
for i,line in enumerate(lines[:6]):
    piece = int(lines[i][0])
    P[piece] = set()
    y = 2
    for L,mystr in enumerate(line.split('\n')[1:]):
        # print(mystr)
        for x in range(3):
            if mystr[x] == '#':
                P[piece].add((x,y))
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
    ax.xaxis.get_major_locator().set_params()
    ax.yaxis.get_major_locator().set_params()
    plt.plot(Xs,Ys,'s')
    return

def move(piece:set[tuple[int, int]], dir) -> set[tuple[int, int]]: # piece = list of coords, dir = (-1,0), ...
    return {(x+dir[0], y+dir[1]) for (x,y) in piece}

def flip(piece:set[tuple[int, int]],f) -> set[tuple[int, int]]: # piece = list of coords, flip horizontally, f = 0,1
    if f == 1:
        return {(2-x, y) for (x,y) in piece}
    else:
        return piece

def rot(piece:set[tuple[int, int]],dir) -> set[tuple[int, int]]: # dir = +1 for CCW, -1 for CW
    CCW = {(0,0):(2,0), (1,0):(2,1), (2,0):(2,2),\
           (0,1):(1,0), (1,1):(1,1), (2,1):(1,2),\
           (0,2):(0,0), (1,2):(0,1), (2,2):(0,2)}
    return {CCW[xy] for xy in piece}

# %% 
def mini_BFS(layout: set) -> int:
    extras = all_spots - layout
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    unusables: int = 0
    # print(f'start: layout: {len(layout)}, extras: {len(extras)}, unusables: {unusables}')
    while extras:
        XX,YY = extras.pop()
        quickvisited: set[tuple[int, int]] = set()
        todo: list[tuple[int, int]] = [(XX,YY)]
        while todo:
            x,y = todo.pop()
            if (x,y) in quickvisited:
                continue
            quickvisited.add((x,y))
            for dir in dirs:
                if x+dir[0] >= 0 and x+dir[0] < Xlim\
                and y+dir[1] >= 0 and y+dir[1] < Ylim\
                and (x+dir[0],y+dir[1]) not in layout:
                    todo.append((x+dir[0],y+dir[1]))
        if len(quickvisited) < 7:
            unusables += len(quickvisited)
            # print(f'unusables: {unusables}')
        extras = extras - quickvisited
    # print(f'unusables: {unusables}')
    # print(f'end: layout: {len(layout)}, extras: {len(extras)}, unusables: {unusables}')
    return unusables


def BFS(piece_pile: list):
    # visited: set[tuple[tuple[tuple[int, int], ...], int, tuple[tuple[int, int], ...]]] = set()
    visited: set[tuple[tuple[int, int],...]] = set()
    todo: list[tuple[set, int, set]] = []
    layout: set[tuple[int, int]] = set()
    cnt = 0
    this_piece = P[piece_pile[cnt]]
    # add the first piece, all orientations with an empty layout
    for dx in range(Xlim-2):
        for dy in range(Ylim-2):
            # every rotaion
            for r in range(4):
                # every flip
                for f in range(2):
                    new_piece = flip(this_piece,f)
                    new_piece = rot(new_piece,r)
                    new_piece = move(new_piece,(dx,dy))
                    todo.append((layout, cnt, new_piece))
    
    print(f'len layout: {len(layout)}, len todo: {len(todo)}')
    counter = 0
    unusables = 0
    while todo:
        if counter % 10000 == 0:
            print(f'counter: {counter}, cnt: {cnt}, len layout: {len(layout)}, len todo: {len(todo)}')
        counter += 1
        # _=[print(x) for x in todo]
        layout, cnt, this_piece = todo.pop(-1)
        # print(f'    pop. len layout: {len(layout)}')
        # if counter == 239:
        #     print(f'counter: {counter}, cnt: {cnt}, len layout: {len(layout)}, len todo: {len(todo)}')

        # if cnt == 2:
        #     print(f'counter: {counter}, cnt: {cnt}, len layout: {len(layout)}, len todo: {len(todo)}')
        #     break

        # check for fit
        if any(coord in layout for coord in this_piece):
            continue

        # check the cache
        # if (tuple(sorted(layout)), cnt, tuple(sorted(this_piece))) in visited:
        #     continue
        # else:
        #     visited.add((tuple(sorted(layout)), cnt, tuple(sorted(this_piece))))           
        
        new_layout = layout.union(this_piece)
        if tuple(sorted(new_layout)) in visited:
            continue
        else:
            visited.add(tuple(sorted(new_layout)))

        # check the unusables
        # print(f'len layout: {len(layout)}')
        unusables = mini_BFS(layout)
        # print(f'unusables: {unusables}')
        if unusables > needed - len(layout):
            continue
        
        # check for done
        if cnt == len(piece_pile)-1: # and not any(coord in layout for coord in this_piece):
            return layout.union(this_piece), cnt+1, True, unusables

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
                        todo.append((new_layout, cnt+1, new_piece))
                        # print(f'len layout: {len(layout)}, len todo: {len(todo)}')

    return layout, cnt, False, unusables

for tree in [trees[2]]:
    print(tree)
    Xlim = tree['XY'][0]
    Ylim = tree['XY'][1]
    # Xlim = 5; Ylim = 4
    all_spots: set[tuple[int, int]] = set([(x,y) for x in range(Xlim) for y in range(Ylim)])
    piece_pile = []
    for i,n_pieces in enumerate(tree['piece_list']):
        for cnt in range(n_pieces):
            piece_pile.append(i)
    needed = 0
    for i in piece_pile:
        needed += len(P[i])
    print(f'needed: {needed}')
    # piece_pile = piece_pile[::-1]
    # piece_pile = [4,4,1,4,3]
    print(f'piece list: {tree["piece_list"]}, piece_pile: {piece_pile}')
    layout, cnt, can_fit, unusables = BFS(piece_pile)
    print(f'len layout: {len(layout)}, cnt: {cnt}, can fit: {can_fit}, unusables: {unusables}')
    unusables = mini_BFS(layout)
    print(f'unusables: {unusables}')
 
    ax = plt.figure().gca()
    print_grid(layout)
    plt.xlim(-.3,Xlim-1+.3)
    plt.ylim(-.3,Ylim-1+.3)
    ax.set_aspect('equal')
    plt.show()

    
