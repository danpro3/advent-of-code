# %%
# part 1

def does_it_repeat(num):
    mystr = str(num)
    mystrlen = len(mystr)
    if mystrlen % 2 == 1:
        return 0
    else:
        if mystr[0:mystrlen//2] == mystr[mystrlen//2:]:
            return num
        else:
            return 0

#  ins = [(x[0], int(x[1:])) for x in open('inputs/input_01_test.txt','r').read().splitlines()]
# groups = open('inputs/input_02_test.txt','r').read().split(',')
groups = open('inputs/input_02.txt','r').read().split(',')
sum_invalids = 0
for i,group in enumerate(groups):
    AB = [int(x) for x in group.split('-')]
    # print(AB)
    IDs = list(range(AB[0],AB[1]+1))
    # print(IDs)
    for ID in IDs:
        sum_invalids += does_it_repeat(ID)
print(f'sum of invalid IDs = {sum_invalids}')

# %% Part 2
import re

def does_it_repeat(num):
    mystr = str(num)
    mystrlen = len(mystr)
    # print(mystr)
    for i in range(mystrlen//2,0,-1):
        pattern = r'('+mystr[0:i]+')'
        matches = re.findall(pattern, mystr)
        sum_repeats = sum([len(match) for match in matches])
        # print(mystr,pattern,matches,sum_repeats)
        if sum_repeats == mystrlen:
            return num
    return 0

#  ins = [(x[0], int(x[1:])) for x in open('inputs/input_01_test.txt','r').read().splitlines()]
# groups = open('inputs/input_02_test.txt','r').read().split(',')
groups = open('inputs/input_02.txt','r').read().split(',')
sum_invalids = 0
for i,group in enumerate(groups):
    AB = [int(x) for x in group.split('-')]
    # print(AB)
    IDs = list(range(AB[0],AB[1]+1))
    # print(IDs)
    for ID in IDs:
        sum_invalids += does_it_repeat(ID)
print(f'sum of invalid IDs = {sum_invalids}')

# 50789015120 is too low
