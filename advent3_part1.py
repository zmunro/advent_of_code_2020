from typing import List

class Spot:
    row: int
    col: int

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col


class TreeGrid:
    base_grid: List[str]

    def __init__(self, tree_grid: List[str]):
        self.base_grid = tree_grid

    def get_grid_height(self):
        return len(self.base_grid)

    def get_coord(self, spot: Spot) -> str:
        assert spot.row <= len(self.base_grid), "row out of bounds"
        col = spot.col % len(self.base_grid[0])
        return self.base_grid[spot.row][col]



input_trees = []
with open("files/advent3_input.txt", "r") as in_f:
    for line in in_f.readlines():
        input_trees.append(line.strip())

trees_hit = 0
tree_grid = TreeGrid(input_trees)
spot = Spot(0, 0)
while True:
    if spot.row >= tree_grid.get_grid_height():
        break
    if tree_grid.get_coord(spot) == "#":
        trees_hit += 1
    spot = Spot(spot.row + 1, spot.col + 3)
print(trees_hit)



















