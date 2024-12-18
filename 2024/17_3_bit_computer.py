# %%
def combo(input):
    if input in [0,1,2,3]:
        return input
    else:
        return regs[input-4]

def run_instruction(opcode,input,i):
    if opcode == 0: # adv
        regs[0] = regs[0]//2**combo(input)
        return i+2

    if opcode == 1: # bxl
        regs[1] = regs[1] ^ input
        return i+2

    if opcode == 2: # bst
        regs[1] = combo(input) % 8
        return i+2

    if opcode == 3: # jnz
        if regs[0] == 0:
            return i+2
        else:
            return input
        
    if opcode == 4: # bxc
        regs[1] = regs[1] ^ regs[2]
        return i+2

    if opcode == 5: # out
        return [i+2, combo(input) % 8]

    if opcode == 6: # bdv 
        regs[1] = regs[0]//2**combo(input)
        return i+2

    if opcode == 7: # cdv
        regs[2] = regs[0]//2**combo(input)
        return i+2

# main
# example:
# A = 729; B = 0; C = 0; prog = [0,1,5,4,3,0]
A = 117440; B = 0; C = 0; prog = [0,3,5,4,3,0] # part 2 makes copy of itself using A=117440
# real input:
# A = 59397658; B = 0; C = 0; prog = [2,4,1,1,7,5,4,6,1,4,0,3,5,5,3,0]

# tester
# A = 10; B = 0; C = 0; prog = [5,0,5,1,5,4]
# A = 2024; B = 0; C = 0; prog = [0,1,5,4,3,0]
# A = 0; B = 2024; C = 43690; prog = [4,0]

regs = [A,B,C]
full_output = []
i = 0
while i < len(prog):
    opcode = prog[i]
    input = prog[i+1]
    # print(f'instruction: {opcode, input}')
    Q = run_instruction(opcode, input,i)
    if opcode == 5: # output is second argument
        full_output.append(Q[1])
        i = Q[0]
    else:
        i = Q
    print(f'i={i} {opcode,input}  output = {full_output}, registers = {regs}')


print(f'output = {full_output}, registers = {regs}')
full_output_str = [str(x) for x in full_output]
full_output = ','.join(full_output_str)
print(f'as a string, output = {full_output}')

# %% part 2

# need to work backwards: find the number that builds the program 
# from the ending up to the beginning

