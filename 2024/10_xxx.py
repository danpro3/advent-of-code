# %%
# filestr = open('inputs/input_09_test.txt','r').read()
filestr = open('inputs/input_09.txt','r').read()
# filestr = filestr[0:100]
num_instr = len(filestr)
print(f'length = {num_instr}, filestr[0:20] = {filestr[0:20]}...{filestr[-20:]}')
# print(f'length = {num_instr}, filestr = {filestr}')
# %%
for i in range(10):
    print(i)
y = ['hello','world']
[print(x) for x in y]