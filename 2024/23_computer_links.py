# %%
from collections import defaultdict

# lines = open("inputs/input_23_test.txt", "r").read().splitlines()
lines = open('inputs/input_23.txt','r').read().splitlines()
# print(lines)

nodes = defaultdict(set)
for line in lines:
    a = line.split("-")
    nodes[a[0]].add(a[1])
    nodes[a[1]].add(a[0])

# _=[print(f'nodes[{x}] = {nodes[x]}') for x in nodes]

# %% part 1 ----------------------------
# look for sets of three
triples = set()

for c1 in nodes:
    for c2 in nodes:
        if c2 != c1:
            s = nodes[c1].intersection(nodes[c2])
            if len(s) > 0 and c2 in nodes[c1] and c1 in nodes[c2]:
                for i in range(len(s)):
                    triples.add(tuple(sorted([c1,c2,s.pop()])))
# _=[print(x) for x in triples]
print(f'number of triples = {len(triples)}')

found_computers = 0
for triple in triples:
    found = False
    i = 0
    while not found and i < 3:
        if triple[i][0] == 't':
            found_computers += 1
            found = True
        i += 1

print(f'found computers starting with "t": {found_computers}')

# %% part 2 -------------------------------------
def check_node(todo):
    added_flag = False
    c1 = todo.pop()
    if c1 in cache:
        return todo
    else:
        cache.append(c1)
    # check the existing groups
    for group in groups:
        if c1 in groups:
            continue
        goodsofar = True
        for g in group:
            if g not in nodes[c1]:
                goodsofar = False
        if goodsofar and {*group,c1} not in groups:
            group.add(c1)
            added_flag = True
            # if len(group) > 2:
            #     print(group)
    # add pairs
    for c2 in nodes[c1]:
        if {c1,c2} not in groups:
            groups.append({c1,c2})
            todo.append(c2)
    return todo

# main
cache = []
groups = []
for c in nodes:
    todo = list(nodes.keys())
    # todo.append()
    while todo:
        # print(todo)
        todo = check_node(todo)
        # print(gr)

# _=[print(x) for x in groups if len(x) > 2]
max_length = 0
max_group = []
for group in groups:
    # print(group)
    if len(group) > max_length:
        max_length = len(group)
        max_group = sorted(group)

print(f'longest group: {max_group}')
max_group = ','.join(max_group)
print(f'longest group: {max_group}')
