grid = [l.strip() for l in open("11.txt", 'r').readlines()]
width, height = len(grid[0]), len(grid)
grid_string = ''.join(grid)

def search_in_direction(grid, row, col, row_dy, col_dx):
    dy = row_dy
    dx = col_dx
    while True:
        if row + dy < 0 or col + dx < 0 or row + dy >= height or col + dx >= width:
            return "."
        if grid[(row + dy) * width + col + dx] != ".":
            return grid[(row + dy) * width + col + dx]
        dy += row_dy
        dx += col_dx

def update_pos(grid, row, col):
    if grid[row * width + col] == ".":
        return "."
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    adjacents = [search_in_direction(grid, row, col, dy, dx) for dy, dx in directions]
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
    if new_grid == grid_string:
        break
    grid_string = new_grid

print(new_grid.count('#'))