instructions = [(l.strip()[0], int(l.strip()[1:])) for l in open("12.txt",'r').readlines()]
pos = [0,0]
facing = 'E'

dir_dict = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}
right_turn = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N'
}
left_turn = {
    'N': 'W',
    'W': 'S',
    'S': 'E',
    'E': 'N'
}

for direction, amount in instructions:
    if direction == 'R':
        for i in range(amount//90):
            facing = right_turn[facing]
        continue
    if direction == 'L':
        for i in range(amount//90):
            facing = left_turn[facing]
        continue
    if direction == 'F':
        pos = pos[0] + dir_dict[facing][0] * amount, pos[1] + dir_dict[facing][1] * amount
    else:
        pos = pos[0] + dir_dict[direction][0] * amount, pos[1] + dir_dict[direction][1] * amount
print(f"Coordinates: {pos}")
print(abs(pos[0]) + abs(pos[1]))