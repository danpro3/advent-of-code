# %%
# groups = open('inputs/input_25_test.txt','r').read().split('\n\n')
groups = open('inputs/input_25.txt','r').read().split('\n\n')

def group_to_seq(group):
    seq = []
    for c in range(len(group[0])):
        count = -1
        for r in range(len(group)):
            if group[r][c] == '#':
                count += 1
        seq.append(count)
    return seq

# print(groups)
locks = []
keys = []
for groupline in groups:
    group = groupline.split('\n')
    seq = group_to_seq(group)
    if group[0].find('.') == -1:
        locks.append(seq)
    else:
        keys.append(seq)
    # print(seq)

combos = 0
for lock in locks:
    for key in keys:
        S = [lock[i] + key[i] for i in range(len(keys[0]))]
        if all([x < 6 for x in S]):
            combos += 1
print(f'combos = {combos}')

