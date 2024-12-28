# %% input

# filestr = open('inputs/input_24_test.txt','r').read().split('\n\n')
# filestr = open('inputs/input_24.txt','r').read().split('\n\n')
filestr = open('inputs/input_24_swaps.txt','r').read().split('\n\n')
wirestrings = filestr[0].splitlines()
gates = filestr[1].splitlines()
for i,gate in enumerate(gates):
    gates[i] = gate.split(' ')
    # print(gate)
wires = dict()
for wirestring in wirestrings:
    wire = wirestring.split(': ')
    wires[wire[0]] = int(wire[1])

# _=[print(x, wires[x]) for x in wires]
# print(gates)

# %% part 1 -----------------------------

def valid_output(wires):
    Zs = [x for x in wires if x[0]=='z']
    if all([wires[x] != None for x in Zs]):
        return True
    else:
        return False

def run_gate(wires, gate):
    # a AND b -> c
    a = gate[0]; instr = gate[1]; b = gate[2]; c = gate[4]
    if wires[a] == None or wires[b] == None:
        return wires
    wires[c] = eval('wires[a]' + operations[instr] + 'wires[b]')
    return wires

def init_wires(wires):
    # initialize the wires
    for gate in gates:
        for i in [0,2,4]:
            # if gate[i] not in wires:
            if gate[i][0] not in ['x','y']:
                wires[gate[i]] = None
    return wires

# main
operations = {'AND':'&', 'OR':'|', 'XOR':'^'}
wires = init_wires(wires)
i = 0
while not valid_output(wires):
    for gate in gates:
        wires = run_gate(wires, gate)
    i += 1
print(f'iterations = {i}')

Zs = sorted([x for x in wires if x[0]=='z'], reverse=True)
# _=[print(wires[x]) for x in Zs]
bin_num = [wires[x] for x in Zs]
print(bin_num)
bin_str = ''.join([str(x) for x in bin_num])
print(f'result = {int(bin_str, base=2)}')

# %% part 2 ---------------------
def list2num(var):
    newlist = sorted([x for x in wires if x[0]==var], reverse=True)
    bin_num = [wires[x] for x in newlist]
    print(bin_num)
    bin_str = ''.join([str(x) for x in bin_num])
    num = int(bin_str, base=2)
    print(f'result = {num}')
    return num

def adder(wires):
    wires = init_wires(wires)
    i = 0
    while not valid_output(wires):
        for gate in gates:
            wires = run_gate(wires, gate)
        i += 1
    print(f'iterations = {i}')
    return list2num('z')

x = list2num('x')
y = list2num('y')
z = adder(wires)
print(f'addlist(x,y) = {x+y}')
print(f'addlist(x,y) - (x+y) = {z-x-y}')

# %%
def find_gate(name,oper):
    i = -1
    found = False
    while not found and i < len(gates)-1:
        i += 1 
        if oper in gates[i] and name in gates[i]:
            if gates[i].index(name) < 3:
                found = True
    if not found:
        print(f'bad wire: {name}')
        baddies.add(name)
    return gates[i], found

xlist = sorted([x for x in wires if x[0]=='x'])
zlist = sorted([x for x in wires if x[0]=='z'])
baddies =set()
for i,xbit in enumerate(xlist):
    # print()
    # level 1 OXR
    gate1, found = find_gate(xbit,'XOR')
    # print(f'xbit: {xbit}, gate1: {gate1}, {found}')

    if xbit == 'x00': # 0th bit
        if gate1[4] != 'z00':
            print(f'bad gate1: {gate1}')
            baddies.add(gate1[4])
            baddies.add('z00')
            break
    else: # needs to go to (^ then done) and (& then | (rest goes with next bit))
        gate2, found = find_gate(gate1[4],'XOR')
        # print(f'xbit: {xbit}, gate2: {gate2}, {found}')
        if not found and gate2[4] != zlist[i]:
            print(f'bad gate2 (ender): {gate2}')
            baddies.add(gate2[4])
            baddies.add(zlist[i])

        gate2, found = find_gate(gate1[4],'AND')
        # print(f'xbit: {xbit}, gate2: {gate2}, {found}')

        gate3, found = find_gate(gate2[4],'OR')
        # print(f'xbit: {xbit}, gate3: {gate3}, {found}')

    # level 1 AND
    gate1, found = find_gate(xbit,'AND')
    # print(f'xbit: {xbit}, gate1: {gate1}, {found}')

    if xbit == 'x00': # 0th bit
        gate2, found = find_gate(gate1[4],'XOR')
        # print(f'xbit: {xbit}, gate1: {gate2}, {found}')
        if gate2[4] != 'z01':
            print(f'bad gate2 (ender): {gate2}')
            baddies.add(gate2[4])
            baddies.add('z01')
            break
        gate2, found = find_gate(gate1[4],'AND')
        # print(f'xbit: {xbit}, gate1: {gate2}, {found}')
    else: # needs to go to ^ then &
        gate3, found = find_gate(gate1[4],'OR')
        # print(f'xbit: {xbit}, gate3: {gate3}, {found}')
        if xbit != xlist[-1]: # not last bit
            gate4, found = find_gate(gate3[4],'XOR')
            # print(f'xbit: {xbit}, gate4: {gate4}, {found}')
            if gate4[4] != zlist[i+1]:
                # print(f'bad gate4 (ender): {gate4}')
                baddies.add(gate4[4])
                baddies.add(zlist[i+1])
                # break
 
        # print(f'{xbit}, baddies: {baddies}')
        if len(baddies) == 2:
            print('need to swap {baddies}')
            break

print(f'{xbit}, baddies: {baddies}')


# %% testing
# keep track of swappers:
# x06, baddies: {'z07', 'bjm'}
# x12, baddies: {'hsw', 'z13'}
# x17, baddies: {'skf', 'z18'}
# gives 0 error for x+y
# x44, baddies: {'nvr', 'z27', 'tdd', 'z35', 'z26', 'wkr'}
# swap nvr, tdd
# swap wkr, nvr

# bjm,hsw,skf,tdd,wkr,z07,z13,z18 is not right

baddies2 = {'z07', 'bjm','hsw', 'z13','skf','z18','tdd','wkr'}
print(baddies2)
password = ','.join(sorted(baddies2))
print(f'password = {password}')
