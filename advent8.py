lines = [[l.split(' ')[0], l.split(' ')[1][0], l.split(' ')[1][1:]] for l in open('8.txt', 'r').readlines()]

def run(game_lines, accumulator = 0, index = 0):
    visited = {x: False for x in range(len(game_lines))}
    while index < len(game_lines) and not visited[index]:
        instruction, direction, amount = game_lines[index]
        visited[index] = True
        index += 1
        if instruction == "acc":
            accumulator += int(amount) if direction == "+" else int(amount) * -1
        if instruction == "jmp":
            index += -1 + (int(amount) if direction == "+" else int(amount) * -1)
    return index == len(game_lines), accumulator


print(f"part 1: {run(lines)[1]}")

for index in range(len(lines)):
    if lines[index][0] == 'nop':
        new_lines = [[x[0], x[1], x[2]] for x in lines]
        new_lines[index][0] = 'jmp'
    elif lines[index][0] == 'jmp':
        new_lines = [[x[0], x[1], x[2]] for x in lines]
        new_lines[index][0] = 'nop'
    else:
        continue
    if run(new_lines)[0]:
        print(f"part 2: {run(new_lines)[1]}")


