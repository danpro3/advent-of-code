# %%
import re
import numpy as np
# lines = open('inputs/input_13_test.txt','r').read().split('\n\n')
lines = open('inputs/input_13.txt','r').read().split('\n\n')
# print(lines)
# %% part 1
total_tokens = 0
for i, line in enumerate(lines):
    Q = [int(x) for x in re.findall('\d+',line)]

    # print(Q)
    A = np.array([[Q[0], Q[2]],[Q[1], Q[3]]]) # coef matrix
    b = np.array([Q[4], Q[5]]) # contant vector
    x = np.linalg.solve(A, b)
    solution = False
    if abs(round(x[0]) - x[0]) < .0000001 or abs(round(x[1]) - x[1]) < .0000001:
        solution = True
        tokens = 3*round(x[0]) + round(x[1])
        # print(tokens)
        total_tokens += tokens
    print(f'i: {i}, solution: {x},{round(x[0])}, {round(x[1])}, {solution}')

print(f'total tokens = {total_tokens}')

# %% part 2
F = 10000000000000
total_tokens = 0
for i, line in enumerate(lines):
    Q = [int(x) for x in re.findall('\d+',line)]

    # print(Q)
    A = np.array([[Q[0], Q[2]],[Q[1], Q[3]]]) # coef matrix
    b = np.array([Q[4]+F, Q[5]+F]) # contant vector
    x = np.linalg.solve(A, b)
    solution = False
    if abs(round(x[0]) - x[0]) < .001 and abs(round(x[1]) - x[1]) < .001:
        solution = True
        tokens = 3*round(x[0]) + round(x[1])
        # print(tokens)
        total_tokens += tokens
    print(f'i: {i}, solution: {x},{round(x[0])}, {round(x[1])}, {solution}')

print(f'total tokens = {total_tokens}')
