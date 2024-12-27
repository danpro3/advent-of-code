# %% input

# filestr = open('inputs/input_24_test.txt','r').read().split('\n\n')
filestr = open('inputs/input_24.txt','r').read().split('\n\n')
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
# b = '0b'+bin_str
print(f'result = {int(bin_str, base=2)}')

