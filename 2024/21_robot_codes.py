# %% part 1
from heapq import heapify, heappop, heappush
from collections import defaultdict

from functools import lru_cache
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

# %%

# @lru_cache
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

code = 'A029A'
visited = set()
npad_paths = set()
npad_dict = dict()
steps = 0
for i in range(len(code)-1):
    pair = code[i:i+2]
    todo = [(steps, npad[code[i]], '')]
    while todo:
        # print(todo)
        todo = move_npad(todo, pair)

# print(npad_paths)
print(npad_dict)

# %% build all paths of npad
def concat(i, code, string, allpaths):
    pair = code[i:i+2]
    if i == len(code)-2:
        if len(npad_dict[pair]) >= 1:
            for k in range(len(npad_dict[pair])):
                newstring = string + npad_dict[pair][k]
                allpaths.append(newstring)
    else:
        if len(npad_dict[pair]) >= 1:
            for k in range(len(npad_dict[pair])):
                concat(i+1,code, string + npad_dict[pair][k],allpaths)
    return allpaths

code = 'A029A'
print(f'code = {code}')
allpaths = concat(0, code, '', [])
print(f'allpaths = {allpaths}')



# %%
npad_dict















# ------------old stuff-----------------------

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

# %%
# create quick dictionary for quickest ways to move on the dpad




# %% move on the dpad given some sequences

def move_dpad(todo, dpad_paths, visited):
    steps, (r, c), seq, path, As = heappop(todo)
    if len(dpad_paths) > 0 and steps > len(next(iter(dpad_paths))):
        return todo
    if path in visited:
        return todo
    else:
        visited.add(path)
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


@lru_cache
def paths_for_dpad(seq):
    print(seq)
    dpad_paths = set()
    # while len(sequences) > 0:
    # seq = sequences.pop()
    todo = [(0, seq[0], seq, '', 0)]
    print('working')
    while todo:
        # print(todo)
        todo = move_dpad(todo, dpad_paths, visited)
    # it = iter(dpad_paths)
    # print(f'length of shortest path: {len(next(it))}')
    # print(f'length of dpad_paths: {len(dpad_paths)}')
    return dpad_paths

# main ---------------
visited = set()
dpad_paths = set()
sequences = ['<A^A^^>AvvvA', '<A^A^>^AvvvA', '<A^A>^^AvvvA']
for sequence in sequences:
    dpad_paths |= paths_for_dpad(sequence)
print(dpad_paths)
# [print(x) for x in dpad_paths]
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

import functools
@functools.lru_cache
def run_robot(level, sequence):
    if level == 2: # end condition: number of robots
        # print(f'seq = {sequence}')
        return len(sequence)
    if sequence in cache:
        return cache[sequence]
    else:
        
        sequences = paths_for_dpad(sequence)
        print(f'sequences = {sequences}')
        npresses_list = []
        for sequence in sequences:
            npresses = 0
            for i in range(len(sequence)-1):
                npresses += run_robot(level+1, sequence[i:i+2])
            npresses_list.append(npresses)
            print(f'npresses = {npresses}')

        # cache[sequence] = min(npresses_list)
        # cache[sequence] = min(run_robot(level+1, seq) for seq in sequences)
    # return cache[sequence]
        return min(npresses_list)

cache = dict()
code = '029A'
npad_paths =  paths_for_npad(code)
print(npad_paths)

npresses_list = []
for i in range(len(next(inter(npad_paths))-1):
    for npad_path in npad_paths:
    npresses = 0
        npresses += run_robot(0, npad_path[i:i+2])
    npresses_list.append(npresses)
    print(f'npresses = {npresses}')

print(f'min npresses = {min(npresses_list)}')

print(f'npresses = {npresses}')
print(f'dpad_paths = {dpad_paths}')
print(f'length of dpad_paths: {len(dpad_paths)}')
it = iter(dpad_paths)
print(f'length of shortest path: {len(next(it))}, {len(next(it))}')

complexity = npresses * int(code[:-1])
print(f'complexity = {complexity}')

# example 029A: length paths = 12, 28, 68

# %%
print(dpad_paths)
ex = 'v<<A>>^A<A>AvA<^AA>A<vAAA>^A'
ex in dpad_paths
print(cache['<A^A^^>AvvvA'])



# def move_dpad(todo, dpad_paths, visited):
#     steps, (r, c), seq, path, As = heappop(todo)
#     if len(dpad_paths) > 0 and steps > len(next(iter(dpad_paths))):
#         return todo
#     if path in visited:
#         return todo
#     else:
#         visited.add(path)
#     # print(seq)
#     if (r,c) == dpad[seq[0]]:
#         just_hit = seq[0]
#         path += 'A'
#         As += 1
#         # print(f'found: seq[0], rest: {seq}, {path}')
#         if len(seq) > 1:
#             seq = seq[1:]
#             while seq[0] == just_hit and len(seq) > 0:
#                 path += 'A'
#                 As += 1
#                 seq = seq[1:]
#             if len(dpad_paths) > 0 and len(path) > len(next(iter(dpad_paths))):
#                 return []
#         else:
#             if len(dpad_paths) > 0 and len(path) > len(next(iter(dpad_paths))):
#                 return []
#             else:
#                 dpad_paths.add(path)
#                 return todo  # return [] for just 1 path
#     for dir in dirs:
#         dr, dc = dir
#         if (r+dr,c+dc) in dpad.values() and (r+dr,c+dc,path) not in visited:
#             # print(f'pushing: {steps + 1, (r+dr,c+dc), (R,C), path+dirs[(dr,dc)]}')
#             heappush(todo, (steps + 1, (r+dr,c+dc), seq, path+dirs[(dr,dc)], As))
#     return todo