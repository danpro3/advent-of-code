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

def move_npad(todo, npad_paths, visited):
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
            if len(npad_paths) > 0 and len(path) > len(next(iter(npad_paths))):
                return []
        else:
            if len(npad_paths) > 0 and len(path) > len(next(iter(npad_paths))):
                return []
            else:
                npad_paths.add(path)
                return todo
    for dir in dirs:
        dr, dc = dir
        if (r+dr,c+dc) in npad.values() and (r+dr,c+dc,path) not in visited:
            # print(f'pushing: {steps + 1, (r+dr,c+dc), (R,C), path+dirs[(dr,dc)]}')
            heappush(todo, (steps + 1, (r+dr,c+dc), code, path+dirs[(dr,dc)]))
    return todo

def paths_for_npad(code):
    visited = set()
    npad_paths = set()
    todo = []
    heappush(todo,(0, npad['A'], code, ''))
    while todo:
        # print(todo)
        todo = move_npad(todo, npad_paths, visited)
    return npad_paths

code = '029A'
npad_paths =  paths_for_npad(code)
print(npad_paths)


# %% move on the dpad given some sequences

def move_dpad(todo, dpad_paths, visited):
    steps, (r, c), seq, path, As = heappop(todo)
    if len(dpad_paths) > 0 and steps > len(next(iter(dpad_paths))):
        return todo
    if (r,c,path) in visited:
        return todo
    else:
        visited.add((r, c, path))
    # print(seq)
    if (r,c) == dpad[seq[0]]:
        just_hit = seq[0]
        path += 'A'
        As += 1
        # print(f'found: seq[0], rest: {seq}, {path}')
        if len(seq) > 1:
            seq = seq[1:]
            while seq[0] == just_hit and len(seq) > 0:
                path += 'A'
                As += 1
                seq = seq[1:]
            if len(dpad_paths) > 0 and len(path) > len(next(iter(dpad_paths))):
                return []
        else:
            if len(dpad_paths) > 0 and len(path) > len(next(iter(dpad_paths))):
                return []
            else:
                dpad_paths.add(path)
                return todo  # return [] for just 1 path
    for dir in dirs:
        dr, dc = dir
        if (r+dr,c+dc) in dpad.values() and (r+dr,c+dc,path) not in visited:
            # print(f'pushing: {steps + 1, (r+dr,c+dc), (R,C), path+dirs[(dr,dc)]}')
            heappush(todo, (steps + 1, (r+dr,c+dc), seq, path+dirs[(dr,dc)], As))
    return todo

# main ---------------

def paths_for_dpad(sequences):
    dpad_paths = set()
    # todo = []
    # heappush(todo,(0, dpad['A'], sequences, ''))
    while len(sequences) > 0:
        visited = set()
        seq = sequences.pop()
        todo = [(0, dpad['A'], seq, '', 0)]
        while todo:
            # print(todo)
            todo = move_dpad(todo, dpad_paths, visited)
        print(seq)
        it = iter(dpad_paths)
        print(f'length of shortest path: {len(next(it))}, {len(next(it))}')
        print(f'length of dpad_paths: {len(dpad_paths)}')
    return dpad_paths

sequences = {'<A^A^^>AvvvA', '<A^A^>^AvvvA', '<A^A>^^AvvvA'}
dpad_paths =  paths_for_dpad(sequences)
print(dpad_paths)
print(f'length of dpad_paths: {len(dpad_paths)}')
it = iter(dpad_paths)
print(f'length of shortest path: {len(next(it))}, {len(next(it))}')
# example: v<<A>>^A<A>AvA<^AA>A<vAAA>^A


#--------gives 28 length-----------------
# all_paths = set()
# START = 'A'
# codes = {'<A^A^^>AvvvA', '<A^A^>^AvvvA', '<A^A>^^AvvvA'}
# while len(codes) > 0:
#     code = codes.pop()
#     visited = set()
#     todo = [(0, dpad[START], code, '', 0)]
#     while todo:
#         # print(todo)
#         todo = move_dpad(todo)
# print(all_paths)
# print(f'length of all_paths: {len(all_paths)}')
# it = iter(all_paths)
# print(f'length of shortest path: {len(next(it))}, {len(next(it))}')




# %%
# how many presses are needed to hit the sequence
# with a further depth of robots, if 
# cache[sequence at depth] = min number

# use the lr cache

# recursion down. start at numpad

