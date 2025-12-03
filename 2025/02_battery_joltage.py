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

# %%
# %% part 1
batteries = open('inputs/input_03_test.txt','r').read().splitlines()
# batteries = open('inputs/input_03.txt','r').read().splitlines()
jolts = 0
targets = ['9','8','7','6','5','4','3','2','1','0']
for battery in batteries:
    nums = []
    idx = -1
    # print(battery)
    for d in range(2,0,-1):
        found = False
        i=0
        while not found:
            # print(f'target = {targets[i]}, battery[:-1] = {battery[:-1]}')
            if targets[i] in battery[idx+1:len(battery)]:
                found = True
                idx = battery[:-1].index(targets[i])
                nums.append(targets[i])
            i += 1
    print(battery,nums)

    # found = False
    # i = 0
    # while not found:
    #     # print(f'target = {targets[i]}, battery[idx+1:] = {battery[idx+1:]}')
    #     if targets[i] in battery[idx+1:]:
    #         found = True
    #         idx2 = battery[idx+1:].index(targets[i])
    #         nums.append(targets[i])
    #     i += 1
    # print('B',battery,ones,idx2)
    # print()
    jolts += int(''.join(nums))
print(f'jolts = {jolts}')
