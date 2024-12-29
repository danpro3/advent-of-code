# %% part 1
from heapq import heapify, heappop, heappush
lines = open('inputs/input_21_test.txt','r').read().splitlines()
# filestr = open('inputs/input_21.txt','r').read().splitlines()
print(lines)
code = lines[0]
print(code)
npad = {'7':(0,0), '8':(0,1), '9':(0,2), \
               '4':(1,0), '5':(1,1), '6':(1,2), \
               '1':(2,0), '2':(2,1), '3':(2,2), \
                '0':(3,1), 'A':(3,2)}
dpad = {'^':(0,1), 'A':(0,2), \
               '<':(1,0), 'v':(1,1), '>':(1,2)}

dirs = {(-1,0):'^', (0,1):'>', (1,0):'v', (0,-1):'<'}
# %% part 1

def move_npad(todo):
    steps, (r, c), code, path = heappop(todo)
    if (r,c,path) in visited:
        return todo
    else:
        visited.add((r, c, path))
    # print(code)
    if (r,c) == npad[code[0]]:
        path += 'A'
        # print(f'found: code[0], rest: {code}, {path}')
        if len(code) > 1:
            code = code[1:]
            if len(all_paths) > 0 and len(path) > len(next(iter(all_paths))):
                return []
        else:
            if len(all_paths) > 0 and len(path) > len(next(iter(all_paths))):
                return []
            else:
                all_paths.add(path)
                return todo
    for dir in dirs:
        dr, dc = dir
        if (r+dr,c+dc) in npad.values() and (r+dr,c+dc,path) not in visited:
            # print(f'pushing: {steps + 1, (r+dr,c+dc), (R,C), path+dirs[(dr,dc)]}')
            heappush(todo, (steps + 1, (r+dr,c+dc), code, path+dirs[(dr,dc)]))
    return todo

visited = set()
all_paths = set()
START = 'A'
code = '029A'
todo = []
heappush(todo,(0, npad[START], code, ''))
while todo:
    # print(todo)
    todo = move_npad(todo)
print(all_paths)


# %% move on the dpad given some code

def move_dpad(todo):
    steps, (r, c), code, path = heappop(todo)
    if (r,c,path) in visited:
        return todo
    else:
        visited.add((r, c, path))
    # print(code)
    if (r,c) == dpad[code[0]]:
        just_hit = code[0]
        path += 'A'
        # print(f'found: code[0], rest: {code}, {path}')
        if len(code) > 1:
            code = code[1:]
            while code[0] == just_hit and len(code) > 0:
                path += 'A'
                code = code[1:]
            if len(all_paths) > 0 and len(path) > len(next(iter(all_paths))):
                return []
        else:
            if len(all_paths) > 0 and len(path) > len(next(iter(all_paths))):
                return []
            else:
                all_paths.add(path)
                return []  # return [] for just 1 path
    for dir in dirs:
        dr, dc = dir
        if (r+dr,c+dc) in dpad.values() and (r+dr,c+dc,path) not in visited:
            # print(f'pushing: {steps + 1, (r+dr,c+dc), (R,C), path+dirs[(dr,dc)]}')
            heappush(todo, (steps + 1, (r+dr,c+dc), code, path+dirs[(dr,dc)]))
    return todo

# main ---------------
all_paths = set()
START = 'A'
codes = {'<A^A^^>AvvvA', '<A^A^>^AvvvA', '<A^A>^^AvvvA'}
while len(codes) > 0:
    code = codes.pop()
    visited = set()
    todo = [(0, dpad[START], code, '')]
    while todo:
        # print(todo)
        todo = move_dpad(todo)
    print(all_paths)
print(f'length of all_paths: {len(all_paths)}')
print(f'length of shortest path: {len(next(iter(all_paths)))}')




# %%
