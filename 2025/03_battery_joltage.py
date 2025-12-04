# %% part 1
# batteries = open('inputs/input_03_test.txt','r').read().splitlines()
batteries = open('inputs/input_03.txt','r').read().splitlines()
jolts = 0
targets = ['9','8','7','6','5','4','3','2','1','0']
for battery in batteries:
    # print(battery)
    found = False
    i=0
    while not found:
        # print(f'target = {targets[i]}, battery[:-1] = {battery[:-1]}')
        if targets[i] in battery[:-1]:
            found = True
            idx = battery[:-1].index(targets[i])
            nums = [targets[i]]
        i += 1
    # print('A',battery,num,idx)

    found = False
    i = 0
    while not found:
        # print(f'target = {targets[i]}, battery[idx+1:] = {battery[idx+1:]}')
        if targets[i] in battery[idx+1:]:
            found = True
            idx2 = battery[idx+1:].index(targets[i])
            nums.append(targets[i])
        i += 1
    # print('B',battery,ones,idx2)
    # print()
    jolts += int(''.join(nums))
print(f'jolts = {jolts}')


# %% part 2
# batteries = open('inputs/input_03_test.txt','r').read().splitlines()
batteries = open('inputs/input_03.txt','r').read().splitlines()
jolts = 0
targets = ['9','8','7','6','5','4','3','2','1','0']
for battery in batteries:
    nums = []
    idx = -1
    n = 12 # number of batteries in each bank: 2 (part1), 12 (part2)
    for d in range(n,0,-1):
        i=0
        while not targets[i] in battery[idx+1:len(battery)-d+1]:
            i += 1
        # print(i,targets[i],battery[idx+1:len(battery)-d+1])
        idx += 1 + battery[idx+1:len(battery)-d+1].index(targets[i])
        nums.append(targets[i])
        # print(idx,nums)

    jolts += int(''.join(nums))
print(f'jolts = {jolts}')

# 171869281139110 is too high


