# %% part 1
# # main
# lines,lines2 = open('inputs/input_05_test.txt','r').read().split('\n\n')
lines,lines2 = open('inputs/input_05.txt','r').read().split('\n\n')
lines = lines.splitlines()
lines2 = lines2.splitlines()

fresh_ranges = []
for line in lines:
    fresh_ranges.append(tuple(int(x) for x in line.split('-')))
# print(fresh_ranges)

IDs = [int(x) for x in lines2]
# print(IDs)

freshIDs = 0
for i,ID in enumerate(IDs):
    for k in range(len(fresh_ranges)):
        if ID >= fresh_ranges[k][0] and ID <= fresh_ranges[k][1]:
            freshIDs += 1
            break
print(f'number of fresh IDs = {freshIDs}')

# %% part 1
# # main
# lines,lines2 = open('inputs/input_05_test.txt','r').read().split('\n\n')
lines,lines2 = open('inputs/input_05.txt','r').read().split('\n\n')
lines = lines.splitlines()

IDs = []
for line in lines:
    IDs.append(list(int(x) for x in line.split('-')))
# print(IDs)

IDs.sort()
# print(IDs)

popped = True
while popped:
    i = 0
    popped = False
    while i < len(IDs)-1:
        # print(f'i = {i}, IDs = {IDs}')
        if IDs[i][1] >= IDs[i+1][0]:
            IDs[i][1] = max(IDs[i][1],IDs[i+1][1])
            IDs.pop(i+1)
            popped = True
        i += 1
    # print(IDs)

diffIDs = [x[1]-x[0]+1 for x in IDs]
# print(f'number of IDs per group = {diffIDs}')
print(f'sum of IDs = {sum(diffIDs)}')

# 352967401360897 is too low
