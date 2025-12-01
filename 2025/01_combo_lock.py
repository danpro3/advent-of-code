# %%
# part 1

#  ins = [(x[0], int(x[1:])) for x in open('inputs/input_01_test.txt','r').read().splitlines()]
# lines = open('inputs/input_01_test.txt','r').read().splitlines()
lines = open('inputs/input_01.txt','r').read().splitlines()
nzeros = 0
loc = 50
for line in lines:
    # print(line)
    if line[0] == 'R':
        loc = (loc + int(line[1:])) % 100
    else:
        loc = (loc - int(line[1:])) % 100
    # print(f'loc = {loc}')
    if loc == 0:
        nzeros += 1
print(f'nzeros = {nzeros}')


# %%

# lines = ['R100','L51']

nzeros = 0
nzeros_stops = 0
loc = 50
for line in lines:
    revs = int(line[1:]) // 100
    clicks = int(line[1:]) % 100

    nzeros += revs
    # print(f'line = {line}, revs = {revs}, clicks = {clicks}')
    if line[0] == 'R':
        new_loc = loc + clicks
        if new_loc == 100:
            nzeros_stops += 1
        if new_loc >= 100:
            nzeros += 1
    else:
        if loc == 0:
            loc = 100
        new_loc = loc - clicks
        if new_loc == 0:
            nzeros_stops += 1
        if new_loc <= 0: 
            new_loc += 100
            nzeros += 1
    # print(f'line = {line}, revs = {revs}, clicks = {clicks}')
    # print(f'loc = {loc}, new_loc = {new_loc}, nzeros = {nzeros}')
    # print()
    loc = new_loc % 100
print(f'nzeros_stops = {nzeros_stops}, nzeros = {nzeros}')

# 5970, 6477, 6492, 
# 5956 is wrong (ignorming 0L)
# 5963 right
