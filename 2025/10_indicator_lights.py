# %% part 1
# lines = open('inputs/input_10_test.txt','r').read().splitlines()
lines = open("inputs/input_10.txt", "r").read().splitlines()
print(f"number of lines = {len(lines)}")
# lines = lines[35:160]

def get_target_code(mystr):
    mapper = {".": "0", "#": "1"}
    binary_list = []
    [binary_list.append(mapper[char]) for char in mystr]
    binary_string = "".join(binary_list[::-1])  # flip endian
    return int(binary_string, 2)


def get_button_codes(mylist):
    buttons = []
    for one_inst in mylist:
        binary_list = [1 << (int(x)) for x in one_inst[1:-1].split(",")]
        buttons.append(sum(binary_list))
    return buttons

Ds = []
for line_num, line in enumerate(lines):
    parts = line.split(" ")
    Ds.append(
        {
            "target": get_target_code(parts[0][1:-1]),
            "buttons": get_button_codes(parts[1:-1]),            
        }
    )

# [print(x) for x in Ds]
# testing
state = 0
D = Ds[0]
for b in [1,3,5,5]:
    state ^= D['buttons'][b]
print(f'target = {D["target"]}, state = {state}')

sum_of_pushes = 0
# BFS search for fastest way to hit the target
def BFS(D):
    state = 0
    pushes = 0
    visited = set()
    todo = [(state, pushes)]
    # print(todo)
    cnt = 0
    while True:
        cnt += 1
        state, pushes = todo.pop(0)
        # todo, pushes, finished = push_button(todo)
        if (state, pushes) in visited:
            continue
        if state == D['target']:
            print(f'Done. state = {state}, pushes = {pushes}')
            return pushes
        else:
            visited.add((state, pushes))
            for B in D['buttons']:
                todo.append((state ^ B, pushes + 1))
# main loop
for D in Ds:
    sum_of_pushes += BFS(D)
    # print(f"                D = {D}")
    print(f"                sum of pushes = {sum_of_pushes}")


# %% part 2
# lines = open('inputs/input_10_test.txt','r').read().splitlines()
lines = open("inputs/input_10.txt", "r").read().splitlines()
print(f"number of lines = {len(lines)}")
# lines = lines[35:160]

def get_target_code(mystr):
    mapper = {".": 0, "#": 1}
    binary_list = []
    [binary_list.append(mapper[char]) for char in mystr]
    return tuple(binary_list)

def get_button_codes(mylist):
    buttons = []
    for one_instr in mylist:
        buttons.append([int(x) for x in one_instr[1:-1].split(',')])
    return buttons

def get_joltage_targets(mylist):
    jolts = [int(x) for x in mylist[1:-1].split(',')]
    return tuple(jolts)

Ds = []
for line_num, line in enumerate(lines):
    parts = line.split(" ")
    Ds.append(
        {
            # "target": get_target_code(parts[0][1:-1]),
            "jolts": get_joltage_targets(parts[-1]),
            "buttons": get_button_codes(parts[1:-1]),
        }
    )

# print(f'length of Ds: {len(Ds)}')
# _ = [print(x) for x in Ds]

import numpy as np
import scipy as sp

total = 0
for D in Ds:
    M = np.zeros((len(D['jolts']),len(D['buttons'])))
    J = np.array(D['jolts'])
    for i,B in enumerate(D['buttons']):
        for b in B:
            M[b][i] = 1
    # print(M, J)

    Z = np.ones((len(D['buttons'])))
    # print(Z.shape, M.shape)
    coef = sp.optimize.linprog(Z, A_eq=M, b_eq=J, bounds=[(0, None) for _ in range(len(Z))], integrality=1 )
    # print(f'coef: {coef.x}, pushes: {sum(coef.x)}')
    total += int(sum(coef.x))

print(f'total: {total}')








# %% NOT USED

def push_button(state,B):
    for b in B:
        state[b] += 1
    return tuple(state)

# BFS search for fastest way to hit the target
def BFS(D):
    state = tuple([0]*len(D['jolts']))
    pushes = 0
    visited = set()
    todo = [(state, pushes)]
    # print(todo)
    cnt = 0
    while True:
        # print(f'                               todo: {todo}')
        cnt += 1
        if cnt % 10000 == 0:
            print(f'cnt = {cnt}, state: {state}, todos: {len(todo)}, visits:{len(visited)}')
        state, pushes = todo.pop(0)
        # print(f'state: {state}, pushes: {pushes}, len todo:{len(todo)}, len visited:{len(visited)}')
        diffs = [D['jolts'][i]-state[i] for i in range(len(state))]
        if any(x < 0 for x in diffs):
            continue
        if (state, pushes) in visited:
            continue
        if state == D['jolts']:
            # print(f'Done. state = {state}, pushes = {pushes}')
            return pushes
        else:
            visited.add((state, pushes))
            for B in D['buttons']:
                # print(f'B:{B}')
                todo.append((push_button(list(state),B), pushes + 1))

# testing
D = Ds[0]
state = tuple([0]*len(D['jolts']))
pushes = 0
# print(f'state:{state}')
# for B in [0,1,1,1,3,3,3,4,5,5]:
#     print(f'state:{D["buttons"][B]}')
#     state = push_button(list(state),D['buttons'][B])
#     print(f'                state:{state}')

# main loop
sum_of_pushes = 0
for D in [Ds[0]]:
    print(f'working on jolts = {D["jolts"]}')
    pushes = BFS(D)
    sum_of_pushes += pushes
    print(f'   joltage:{D["jolts"]}, pushes: {pushes}, sum of pushes: {sum_of_pushes}')

