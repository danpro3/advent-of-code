# %% part 1
lines = open('inputs/input_08_test.txt','r').read().splitlines()
# lines = open('inputs/input_08.txt','r').read().splitlines()
npairs = 10  # test
# npairs = 1000 # real input

boxes = []
for i, line in enumerate(lines):
    boxes.append([int(x) for x in line.split(',')])

# find distances and sort
n = len(boxes)
# print(boxes)
pairs = []
for a in range(n-1):
    for b in range(a+1,n):
        D = 0
        for i in range(3):
            D += (boxes[a][i] - boxes[b][i])**2
        pairs.append((D,a,b))
pairs.sort(key=lambda sublist: sublist[0],reverse=False)
# _=[print(x) for x in pairs[:5]]

# build circuits
circuits = []
for i in range(npairs):
    D,j0,j1 = pairs.pop(0)
    # print(j0,j1)

    # find pre-existing junction boxes in the circuit
    found = [-1,-1]  # circuit number for the pair j1,j2    
    for a in range(len(circuits)):
        if j0 in circuits[a]:
            found[0] = a
        if j1 in circuits[a]:
            found[1] = a
    # print(found)
    # add in the j-boxes
    if found == [-1,-1]:
        circuits.append(set([j0,j1]))
    elif found[0] != -1 and found[1] == -1:
        circuits[found[0]].add(j1)
    elif found[0] == -1 and found[1] != -1:
        circuits[found[1]].add(j0)
    elif found[0] != found[1]: # combine 2 circuits
        found.sort(reverse=True)
        A = circuits.pop(found[0])
        B = circuits.pop(found[1])
        circuits.append(set(list(A)+list(B)))

# print(circuits)
circuit_lengths = [len(x) for x in circuits]
circuit_lengths.sort(reverse=True)
# print(circuit_lengths)
print(f'longest 3 circuits are ',circuit_lengths[:3])
print(f'product = {circuit_lengths[0]*circuit_lengths[1]*circuit_lengths[2]}')

# %% part 2
# lines = open('inputs/input_08_test.txt','r').read().splitlines()
lines = open('inputs/input_08.txt','r').read().splitlines()

boxes = []
for i, line in enumerate(lines):
    boxes.append([int(x) for x in line.split(',')])

# find distances and sort
n = len(boxes)
# print(boxes)
pairs = []
for a in range(n-1):
    for b in range(a+1,n):
        D = 0
        for i in range(3):
            D += (boxes[a][i] - boxes[b][i])**2
        pairs.append((D,a,b))
pairs.sort(key=lambda sublist: sublist[0],reverse=False)
# _=[print(x) for x in pairs[:5]]

# build circuits
circuits = []
c = 0
while c < len(pairs):
    # print(c,len(pairs))
    D,j0,j1 = pairs.pop(0)
    # print(j0,j1)

    # find pre-existing junction boxes in the circuit
    found = [-1,-1]  # circuit number for the pair j1,j2    
    for a in range(len(circuits)):
        if j0 in circuits[a]:
            found[0] = a
        if j1 in circuits[a]:
            found[1] = a
    # print(found)
    # add in the j-boxes
    if found == [-1,-1]:
        circuits.append(set([j0,j1]))
    elif found[0] != -1 and found[1] == -1:
        circuits[found[0]].add(j1)
    elif found[0] == -1 and found[1] != -1:
        circuits[found[1]].add(j0)
    elif found[0] != found[1]: # combine 2 circuits
        found.sort(reverse=True)
        A = circuits.pop(found[0])
        B = circuits.pop(found[1])
        circuits.append(set(list(A)+list(B)))
    # print(circuits)
    # print(f'len(boxes) = {len(boxes)}, length of circuit[0] = {len(circuits[0])}')
    # print()
    if len(circuits[0]) == len(boxes):
        print(f'done at c = {c}')
        break
    c += 1

print(boxes[j0])
print(boxes[j1])
print(f'mult of x  = {boxes[j0][0]*boxes[j1][0]}')