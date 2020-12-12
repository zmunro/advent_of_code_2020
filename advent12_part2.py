instructions = [(l.strip()[0], int(l.strip()[1:])) for l in open("12.txt",'r').readlines()]
pos_x, pos_y = 0,0
waypoint_dif_x, waypoint_dif_y = 10, 1

dir_dict = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

for direction, amount in instructions:
    if direction == 'R':
        for i in range(amount//90):
            waypoint_dif_x, waypoint_dif_y = waypoint_dif_y, waypoint_dif_x * -1
    elif direction == 'L':
        for i in range(amount//90):
            waypoint_dif_x, waypoint_dif_y = waypoint_dif_y * -1, waypoint_dif_x
    elif direction == 'F':
        pos_x, pos_y = pos_x + amount * waypoint_dif_x, pos_y + amount * waypoint_dif_y
    else:
        waypoint_dif_x = waypoint_dif_x + dir_dict[direction][0] * amount
        waypoint_dif_y  = waypoint_dif_y + dir_dict[direction][1] * amount

print(f"Coordinates: {pos_x , pos_y}")
print(abs(pos_x) + abs(pos_y))