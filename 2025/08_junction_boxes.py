# %% part 1
lines = open('inputs/input_08_test.txt','r').read().splitlines()
# lines = open('inputs/input_08.txt','r').read().splitlines()

boxes = []
for i, line in enumerate(lines):
    boxes.append([int(x) for x in line.split(',')])

# find distances and sort
n = len(boxes)
print(boxes)
dists = []
for a in range(n-1):
    for b in range(a+1,n):
        D = 0
        for i in range(3):
            D += (boxes[a][i] - boxes[b][i])**2
        dists.append((D,a,b))
dists.sort(key=lambda sublist: sublist[0],reverse=False)
_=[print(x) for x in dists[:5]]

# build circuits
circuits = dict()
c = 0
for i in range(10):
    D,j1,j2 = dists.pop(0)
    print(j1,j2)
    if j1 in circuits:
        circuits[j1].append






