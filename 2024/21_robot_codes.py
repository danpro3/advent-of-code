# %% part 1
lines = open('inputs/input_21_test.txt','r').read().splitlines()
# filestr = open('inputs/input_21.txt','r').read().splitlines()
print(lines)

# %% part 1

npad = [['7','8','9'], ['4','5','6'], ['1','2','3'], ['','0','A']]
dpad = [['','^','A'], ['<','v','>']]

state = (r1,c1,r2,c2,r3,c3,seq)

def pushbutton(state):
    r1,c1,r2,c2,r3,c3,seq = state


for line in lines:
