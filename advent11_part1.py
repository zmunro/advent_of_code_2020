grid = [l.strip() for l in open("11.txt", 'r').readlines()]
width = len(grid[0])
height = len(grid)
grid_string = ''.join(grid)

def update_pos(grid, row, col):
    adjacents = []
    for i,j in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        if row + i >= 0 and col + j >= 0 and row + i < height and col + j < width:
            adjacents.append(grid[(row + i) * width + col + j])
    if grid[row * width + col] == 'L' and adjacents.count('#') == 0:
        return '#'
    if grid[row * width + col] == '#' and adjacents.count('#') >= 4:
        return 'L'
    return grid[row * width + col]


while True:
    new_grid = list(grid_string)
    for row in range(height):
        for col in range(width):
            new_grid[row * width + col] = update_pos(grid_string, row, col)
    new_grid_string = ''.join(new_grid)
    if new_grid_string == grid_string:
        break
    grid_string = new_grid_string

print(new_grid_string.count('#'))