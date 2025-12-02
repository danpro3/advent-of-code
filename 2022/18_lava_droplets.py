# %% lava droplets
cubes = open('inputs/input_18_test.txt').read().splitlines()
# print(cubes)
for i,cube in enumerate(cubes):
    cubes[i] = [int(x) for x in cube.split(',')]
print(cubes)

x,y,z = zip(*cubes)
print(x,y,z)
for i,cube in enumerate(cubes):
    # for k,cube2 in enumerate(cubes2):
    print(i)
    a = cubes[i+1:].index(cubes[i][1])
    print(a)

