# %% part 1
# lines = open('inputs/input_07_test.txt','r').read().splitlines()
lines = open('inputs/input_07.txt','r').read().splitlines()

grid = [list(line) for line in lines]
# _=[print(x) for x in grid]
start = lines[0].index('S')
# print(start)

splits = 0
beams = {start}
new_beams = set()
for r in range(1,len(lines)):
    while len(beams) > 0:
        c = beams.pop()
        if grid[r][c] == '^':
            splits += 1
            new_beams.add(c-1)
            new_beams.add(c+1)
        else:
            new_beams.add(c)
    beams = new_beams.copy()
    new_beams = set()
    # print(f'r={r},beams={beams}')
print(f'number of beams = {len(beams)}')
print(f'number of splits = {splits}')

# %% part 2
# lines = open('inputs/input_07_test.txt','r').read().splitlines()
lines = open('inputs/input_07.txt','r').read().splitlines()

grid = [list(line) for line in lines]
# _=[print(''.join(x)) for x in grid[:6]]
start = lines[0].index('S')
# print(start)

timelines = 0
splits = 0
beams = {start:1}
new_beams = {}
for r in range(1,len(lines)):
    while len(beams) > 0:
        c,n = beams.popitem()  # column and how many paths got there
        # print(f'popping {c,n}')
        if grid[r][c] == '^':
            splits += 1
            if c-1 in new_beams:
                new_beams[c-1] += n
            else:
                new_beams[c-1] = n
            if c+1 in new_beams:
                new_beams[c+1] += n
            else:
                new_beams[c+1] = n
        else:
            if c in new_beams:
                new_beams[c] += n
            else:
                new_beams[c] = n
        # print(f'r,c={r,c},splits = {splits}, beams={beams}, new_beams = {new_beams}')
    beams = new_beams.copy()
    new_beams = {}
    # print()

print(f'number of beams = {len(beams)}')
print(f'number of splits = {splits}')
all_values = beams.values()
# print(f'n total = {sum(all_values)}, values = {all_values}')
print(f'num total timelines = {sum(all_values)}')
