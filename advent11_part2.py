grid = [l.strip() for l in open("11.txt", 'r').readlines()]
width = len(grid[0])
height = len(grid)
grid_string = ''.join(grid)
# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.
# Floor (.) never changes; seats don't move, and nobody sits on the floor.

def main(grid_string):
    while True:
        # for i in range(height):
        #     print(grid_string[i * width: i * width + width])
        # print('----------------------------------')
        # input()
        new_grid = list(grid_string)
        for row in range(height):
            for col in range(width):
                new_grid[row * width + col] = update_pos(grid_string, row, col)

        new_grid_string = ''.join(new_grid)
        if new_grid_string == grid_string:
            break
        grid_string = new_grid_string

    print(new_grid_string.count('#'))

def update_pos(grid, row, col):
    adjacent_moves = [
        (-1,-1),
        (-1,0),
        (-1,1),
        (0,-1),
        (0,1),
        (1,-1),
        (1,0),
        (1,1)
    ]
    adjacents = []
    for i,j in adjacent_moves:
        try:
            if row + i >= 0 and col + j >= 0 and row + i < height and col + j < width:
                adjacents.append(grid[(row + i) * width + col + j])
        except:
            continue
    adj_str = ''.join(adjacents)
    if grid[row * width + col] == 'L' and adj_str.count('#') == 0:
        return '#'
    if grid[row * width + col] == '#' and adj_str.count('#') >= 4:
        return 'L'
    return grid[row * width + col]


main(grid_string)