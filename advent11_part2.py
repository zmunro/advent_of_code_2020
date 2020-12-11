grid = [l.strip() for l in open("11.txt", 'r').readlines()]
width = len(grid[0])
height = len(grid)
grid_string = ''.join(grid)

def search_in_direction(grid, row, col, row_dx, col_dx):
    r_dx = row_dx
    c_dx = col_dx
    while True:
        if row + r_dx < 0 or col + c_dx < 0 or row + r_dx >= height or col + c_dx >= width:
            return "."
        if grid[(row + r_dx) * width + col + c_dx] != ".":
            return grid[(row + r_dx) * width + col + c_dx]
        r_dx += row_dx
        c_dx += col_dx

def update_pos(grid, row, col):
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    adjacents = [search_in_direction(grid, row, col, i, j) for i,j in directions]
    if grid[row * width + col] == 'L' and adjacents.count('#') == 0:
        return '#'
    if grid[row * width + col] == '#' and adjacents.count('#') >= 5:
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