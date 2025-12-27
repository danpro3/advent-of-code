# %% part 1
# lines = open('inputs/input_10_test.txt','r').read().splitlines()
lines = open("inputs/input_10.txt", "r").read().splitlines()
print(f"number of lines = {len(lines)}")
# lines = lines[35:160]


def get_target_code(mystr):
    mapper = {".": "0", "#": "1"}
    binary_list = []
    [binary_list.append(mapper[char]) for char in mystr]
    binary_string = "".join(binary_list[::-1])  # flip endian
    return int(binary_string, 2)


def get_button_codes(mylist):
    buttons = []
    for one_inst in mylist:
        binary_list = [1 << (int(x)) for x in one_inst[1:-1].split(",")]
        buttons.append(sum(binary_list))
    return buttons


sum_of_pushes = 0
D = []
for line_num, line in enumerate(lines):
    # print(line)
    parts = line.split(" ")
    # print(parts[0][1:-1])

    D.append(
        {
            "target": get_target_code(parts[0][1:-1]),
            "buttons": get_button_codes(parts[1:-1]),
            
        }
    )

    # print(f'target = {target} = {bin(target)}')
    # print(f'buttons = {parts[1:-1]}')
    # print(f'buttons = {[bin(x) for x in buttons]}')
    # print(f'buttons = {buttons} = {[bin(x) for x in buttons]}')

    # testing
    # state = 0
    # for b in [1,3,5,5]:
    #     state ^= buttons[b]
    # print(f'terget = {target}, state = {state}')

    # BFS search for fastest way to hit the target
    def push_button(todo):
        state, pushes = todo.pop(0)
        if (state, pushes) in visited:
            return todo, pushes, False
        if state == target:
            # print(f'Done. state = {state}, pushes = {pushes}')
            return todo, pushes, True
        else:
            visited.add((state, pushes))
            for B in buttons:
                todo.append((state ^ B, pushes + 1))
        return todo, pushes, False

    state = 0
    pushes = 0
    visited = set()
    todo = [(state, pushes)]
    # print(todo)
    finished = False
    cnt = 0
    while not finished and len(todo) > 0:
        cnt += 1
        todo, pushes, finished = push_button(todo)
        # print(todo)
        # print(visited)
        # print()
    # print(f'length of visited = {len(visited)}')
    # print(visited)

    sum_of_pushes += pushes
print(
    f"line: {line_num}, visited: {len(visited)}, pushes: {pushes}  sum of pushes = {sum_of_pushes}"
)
