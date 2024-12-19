# %%
def combo(input):
    if input in [0,1,2,3]:
        return input
    else:
        return regs[input-4]

def run_instruction(regs, opcode,input,i):
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
# A = 117440; B = 0; C = 0; prog = [0,3,5,4,3,0] # part 2 makes copy of itself using A=117440
# A = 0o3453
# A = 0o35000

# real input:
A = 59397658; B = 0; C = 0; prog = [2,4,1,1,7,5,4,6,1,4,0,3,5,5,3,0]
# A = 0o355304164571142000
# A = 0o1
# 2,4 is B = A % 8
# 1,1 B = B xor 1 flips the right bit
# 7,5 C = A//2^(B)
# 4,6 B = B xor C
# 1,4 B = B xor A+
# 0,3
# 5,5 output B % 8
# 3,0 jump back to beginning unless A == 0

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
    Q = run_instruction(regs, opcode, input,i)
    if opcode == 5: # output is second argument
        full_output.append(Q[1])
        i = Q[0]
    else:
        i = Q
    # print(f'i={i} {opcode,input}  output = {full_output}, registers = {regs}')

del i
print(f'input = {A}')
print(f'output = {full_output}, registers = {regs}')
full_output_str = [str(x) for x in full_output]
full_output = ','.join(full_output_str)
# print(f'as a string, output = {full_output}')

# %% part 2 -----------------------------------------------------------------------------------

# need to work backwards: find the number that builds the program 
# from the ending up to the beginning
def run_program(regs, prog):
    full_output = []
    a = 0
    while a < len(prog):
        opcode = prog[a]
        input = prog[a+1]
        # print(f'instruction: {opcode, input}')
        Q = run_instruction(regs, opcode, input,a)
        if opcode == 5: # output is second argument
            full_output.append(Q[1])
            a = Q[0]
        else:
            a = Q
    return full_output

def find_one_digit(todo):
    workingA, digit = todo.pop()
    if digit < 0:
        print(f'totally done: {workingA}')
    k = 0
    while k < 8:
        A = workingA + k*8**(digit-1)
        regs = [A, 0, 0]
        output = run_program(regs, prog)
        sublist = output[digit-N-1:]
        needlist = prog[digit-N-1:]
        print(f'{oct(A)} -> {output}, {sublist}, need: {needlist}')
        if sublist == needlist:
            workingA = A
            digit -= 1
            todo.append((A,digit))
            print(f'got it: so far: A = {oct(A)}')
        k += 1
    return todo

# main --------------
# A = 729; B = 0; C = 0; prog = [0,1,5,4,3,0]
# A = 117440; B = 0; C = 0; prog = [0,3,5,4,3,0] # part 2 makes copy of itself using A=117440
# A = 0o345300
# A = 0o35000

# real input:
A = 59397658; B = 0; C = 0; prog = [2,4,1,1,7,5,4,6,1,4,0,3,5,5,3,0]
regs = [A, B, C]
# A = 0o2
# initial check
output = run_program(regs, prog)
print(f'{oct(A)} -> {output}')
print()

print(f'{prog}')
N = len(prog)
todo = [(0,N)]
winners = []
del regs
while todo:
    A, digit = todo[0]
    todo = find_one_digit(todo)
# print(f'digit = {digit}, A = {oct(A)}, A = {A}')

# final check
regs = [A, B, C]
output = run_program(regs, prog)
print()
print(f'program: {prog}')
print(f'output:  {output}')
# TO LOW: digit = 3, A = 0o5600644674024000, A = 202366627358720

# %%
A = 59397658; B = 0; C = 0; prog = [2,4,1,1,7,5,4,6,1,4,0,3,5,5,3,0]
A = 0o0
regs = [A, B, C]
output = run_program(regs, prog)
print(f'A = {A} = {oct(A)} -> {output}')


# %%
print(f'{prog}')
done = False
N = len(prog)
digit = N
workingA = 0
todo = []
winners = []
while digit > 2 and not done:
    found = False
    i = 0
    while i < 8 and not found:
        A = workingA + i*8**(digit-1)
        regs = [A, B, C]
        output = run_program(regs, prog)
        sublist = output[digit-N-1:]
        needlist = prog[digit-N-1:]
        print(f'{oct(A)} -> {output}, {sublist}, need: {needlist}')
        if sublist == needlist:
            found = True
            workingA = A
            digit -= 1
            print(f'got it: so far: A = {oct(A)}')
        i += 1
print(f'digit = {digit}, A = {oct(A)}, A = {A}')

regs = [A, B, C]
output = run_program(regs, prog)
print(f'program: {prog}')
print(f'output:  {output}')
# TO LOW: digit = 3, A = 0o5600644674024000, A = 202366627358720
