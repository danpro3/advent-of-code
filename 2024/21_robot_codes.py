# %% part 1
from heapq import heapify, heappop, heappush
from collections import defaultdict

from functools import lru_cache
# codes = open('inputs/input_21_test.txt','r').read().splitlines()
codes = open('inputs/input_21.txt','r').read().splitlines()
print(codes)
npad = {'7':(0,0), '8':(0,1), '9':(0,2), \
               '4':(1,0), '5':(1,1), '6':(1,2), \
               '1':(2,0), '2':(2,1), '3':(2,2), \
                '0':(3,1), 'A':(3,2)}
dpad = {'^':(0,1), 'A':(0,2), \
               '<':(1,0), 'v':(1,1), '>':(1,2)}

dirs = {(-1,0):'^', (0,1):'>', (1,0):'v', (0,-1):'<'}

# %% ---------------  build dictionary of npad -------------------

def move_npad(todo, pair):
    steps, (r, c), path = heappop(todo)
    if (r,c) == npad[pair[1]]:
        path += 'A'
        if pair not in npad_dict:
            print(f'Adding: {pair}, {path}')
            npad_dict[pair] = [path]
        else:
            if len(path) > len(next(iter(npad_dict[pair]))):
                return []
            else:
                print(f'Adding: {pair}, {path}')
                npad_dict[pair].append(path)
                return todo
    for dir in dirs:
        dr, dc = dir
        if (r+dr,c+dc) in npad.values():
            # print(f'pushing: {steps + 1, (r+dr,c+dc), (R,C), path+dirs[(dr,dc)]}')
            heappush(todo, (steps + 1, (r+dr,c+dc), path+dirs[(dr,dc)]))
    return todo

def add_to_npad_dict(pair):
    todo = [(0, npad[pair[0]], '')]
    while todo:
        todo = move_npad(todo, pair)
    return

code = 'A029A'
visited = set()
npad_paths = set()
npad_dict = dict()
steps = 0
for i in range(len(code)-1):
    pair = code[i:i+2]
    add_to_npad_dict(pair)

# print(npad_paths)
print(npad_dict)

# %% ---------- test build all paths of npad --------------------
def concat_npad(i, code, string, allpaths):
    pair = code[i:i+2]
    if i == len(code)-2:
        if len(npad_dict[pair]) >= 1:
            for k in range(len(npad_dict[pair])):
                newstring = string + npad_dict[pair][k]
                allpaths.append(newstring)
    else:
        if len(npad_dict[pair]) >= 1:
            for k in range(len(npad_dict[pair])):
                concat_npad(i+1,code, string + npad_dict[pair][k],allpaths)
    return allpaths

code = 'A029A'
print(f'code = {code}')
allpaths = concat_npad(0, code, '', [])
print(f'num allpaths = {len(allpaths)}')
print(f'length of each allpaths = {len(next(iter(allpaths)))}')
# print(f'allpaths = {allpaths}')


# %% --------   build dictionary of dpad  ------------------

def move_dpad(todo, pair):
    steps, (r, c), path = heappop(todo)
    if (r,c) == dpad[pair[1]]:
        path += 'A'
        if pair not in dpad_dict:
            print(f'Adding: {pair}, {path}')
            dpad_dict[pair] = [path]
        else:
            if len(path) > len(next(iter(dpad_dict[pair]))):
                return []
            else:
                if path not in dpad_dict[pair]:
                    print(f'Adding: {pair}, {path}')
                    dpad_dict[pair].append(path)
                return todo
    for dir in dirs:
        dr, dc = dir
        if (r+dr,c+dc) in dpad.values():
            # print(f'pushing: {steps + 1, (r+dr,c+dc), (R,C), path+dirs[(dr,dc)]}')
            heappush(todo, (steps + 1, (r+dr,c+dc), path+dirs[(dr,dc)]))
    return todo

def add_to_dpad_dict(pair):
    todo = [(0, dpad[pair[0]], '')]
    while todo:
        todo = move_dpad(todo, pair)
    return

path = 'A<A^A>^^AvvvA<A^A^>^AvvvA<A^A^^>AvvvA>><^'
visited = set()
dpad_paths = set()
dpad_dict = dict()
steps = 0
for i in range(len(path)-1):
    pair = path[i:i+2]
    add_to_dpad_dict(pair)

# print(dpad_paths)
print(dpad_dict)

# %% ------------ test dpad paths -------------------------
def concat_dpad(i, path, string, allpaths):
    pair = path[i:i+2]
    if i == len(path)-2:
        if len(dpad_dict[pair]) >= 1:
            for k in range(len(dpad_dict[pair])):
                newstring = string + dpad_dict[pair][k]
                # if len(allpaths) > 0 and len(newstring) == len(next(iter(allpaths))):
                allpaths.add(newstring)
    else:
        if len(dpad_dict[pair]) >= 1:
            for k in range(len(dpad_dict[pair])):
                concat_dpad(i+1,path, string + dpad_dict[pair][k],allpaths)
    return allpaths

paths = ['A<A^A>^^AvvvA', 'A<A^A^>^AvvvA', 'A<A^A^^>AvvvA']
allpaths = set()
allpaths_lengths = []
for path in paths:
    print(f'path = {path}')
    allpaths = concat_dpad(0, path, '', allpaths)
    print(f'num allpaths = {len(allpaths)}')
    print(f'length of each allpaths = {len(next(iter(allpaths)))}')
    for i in range(len(allpaths)):
        allpaths_lengths.append(len(next(iter(allpaths))))
#     print(allpaths_lengths)
# print(f'allpaths = {allpaths}')

# %% -----------  recursion - main loop -------------

@lru_cache
def tell_robot(layer, path):
    path = 'A'+path
    if layer == NUM_ROBOTS:
        return len(path)-1
    total_presses = 0
    for i in range(len(path)-1):
        if path[i:i+2] not in dpad_dict:
            add_to_dpad_dict(path[i:i+2])
        newpaths = dpad_dict[path[i:i+2]]
        presses = []
        for newpath in newpaths:
            # print(f'dpad path: {newpath}, paths: {newpaths}')
            presses.append(tell_robot(layer+1, newpath))
        # print(f'all presses: {presses}')
        total_presses += min(presses)
    return total_presses

# main
NUM_ROBOTS = 26  # 3 for example, 26 for real input
complexity = 0
for code in codes:
    code = 'A' + code
    total_presses = 0
    # print(f'code: {code}')
    for i in range(len(code)-1):
        if code[i:i+2] not in npad_dict:
            add_to_npad_dict(code[i:i+2])
        paths = npad_dict[code[i:i+2]]
        # print(f'       npad pair: {code[i:i+2]}, paths: {paths}')
        presses = []
        for path in paths:
            presses.append(tell_robot(1, path))
            # print(f'       path = {path}, presses = {presses}')
        total_presses += min(presses)
    complexity += total_presses*int(code[1:-1])
    print(f'code: {code}, presses: {total_presses}')

print(f'complexity = {complexity}')
