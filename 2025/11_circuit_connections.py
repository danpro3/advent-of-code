# %% part 1

# lines = open('inputs/input_11_test.txt','r').read().splitlines()
lines = open("inputs/input_11.txt", "r").read().splitlines()
print(f"number of lines = {len(lines)}")

D = {}
for line in lines:
    D[line.split(': ')[0]] = [x for x in line.split(': ')[1].split(' ')]
# for key, value in D.items():
#     print(f"{key}: {value}")

def BFS(D):
    npaths = 0
    todo = [('','you')]
    while len(todo) > 0:
        path = todo.pop(0)
        if path[-1] == 'out':
            # print(f'done. path: {path}')
            npaths += 1
        else:
            for next in D[path[-1]]:
                # print(f'adding: {next}')
                todo.append(tuple(list(path) + [next]))
    return npaths

npaths = BFS(D)
print(f'n paths: {npaths}')

# %% part 2
# import os
# print(os.getcwd())
# lines = open('inputs/input_11_test_2.txt','r').read().splitlines()
lines = open("inputs/input_11.txt", "r").read().splitlines()
print(f"number of lines = {len(lines)}")

D = {}
for line in lines:
    D[line.split(': ')[0]] = [x for x in line.split(': ')[1].split(' ')]
# for key, value in D.items():
#     print(f"{key}: {value}")


# %% part 2
from functools import lru_cache

@lru_cache
def move(node):
    npaths = {'out':0, 'dac':0, 'fft':0, 'both':0}
    if node == 'out':
        npaths['out'] += 1
        return npaths
    for next in D[node]:
        npaths_child = move(next)
        npaths = {k:v+npaths_child.get(k) for k,v in npaths.items()} 
    if node == 'dac':
        npaths['dac'] = npaths['out']
        npaths['both'] = npaths['fft']
    if node == 'fft':
        npaths['fft'] = npaths['out']
        npaths['both'] = npaths['dac']
    # print(f'{node} returning: {npaths}')
    return npaths

npaths = move('svr')
print(f'n paths: {npaths}')
