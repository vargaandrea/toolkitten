# Let's assume that the total area of two super continents is a random integer from 30 to 60.
import random

two_continent_area = random.randint(30, 60)

# The minimum continent area is 15. Let's calculate area of the first continent

first_area = random.randint(15, two_continent_area)

# The area of the second continent shall be the rest of two_continent_area

second_area = two_continent_area - first_area


# Create grid

def create_row(w):
    line = [["O"] for i in range(w)]
    return line


def create_grid(h, w):
    grid = [create_row(w) for i in range(h)]
    return grid


height = 11
width = 11

game_field = create_grid(height, width)

# Chose random start point for the first continent in the upper half of the field and start point
# for the second continent in the lower half of the field. We will have not less than 2 free tiles between these points
x1 = random.randint(1, int(width/2)-1)
y1 = random.randint(1, int(height/2-1))


x2 = random.randint((int(width/2)+1), width-1)
y2 = random.randint((int(height/2)+1), height-1)

# Put "X" in each of the start points

game_field[y1][x1] = ["X"]

game_field[y2][x2] = ["X"]

# First continent can never touch the second continent so let's make a list of "forbidden cells".
# We will check if these cells are within the grid


def cells_around(coord_y, coord_x, w, h, new_list):
    if (coord_y-1) >= 0:
        if (coord_x-1) >= 0:
            new_list.append([coord_y - 1, coord_x - 1])
            new_list.append([coord_y - 1, coord_x])
        if (coord_x+1) < w:
            new_list.append([coord_y - 1, coord_x + 1])
    if (coord_x-1) >= 0:
        new_list.append([coord_y, coord_x - 1])
    if (coord_x+1) < w:
        new_list.append([coord_y, coord_x + 1])
    if (coord_y+1) < h:
        if (coord_x-1) >= 0:
            new_list.append([coord_y + 1, coord_x - 1])
            new_list.append([coord_y + 1, coord_x])
        if (coord_x+1) < w:
            new_list.append([coord_y + 1, coord_x + 1])


forbidden_cells = []
cells_around(y2, x2, width, height, forbidden_cells)



# Let's build the first continent
# The second tile of the first continent should be in the allowed_cells
allowed_cells = []
cells_around(y1, x1, width, height, allowed_cells)

while first_area > 0:
    # Delete all possible "X" from allowed_cells. Delete possible forbidden cells
    to_delete = []
    for i in range(len(allowed_cells)):
        if allowed_cells[i] == ["X"]:
            to_delete.append(allowed_cells[i])
        if allowed_cells[i] in forbidden_cells and allowed_cells[i] != ["X"]:
            to_delete.append(allowed_cells[i])
    # for i in to_delete:
    #     ind = allowed_cells.index(to_delete[i])
    #     del allowed_cells[ind]

    # Random cell to place next tile
    new_cell_num = random.randint(0, len(allowed_cells)-2)
    new_cell = allowed_cells[new_cell_num]
    # Replace with "X" and delete it from allowed_cells
    game_field[new_cell[0]][new_cell[1]] = ["X"]
    del allowed_cells[new_cell_num]
    # Add new cells to allowed_cells
    cells_around(new_cell[0], new_cell[1], width, height, allowed_cells)
    first_area -= 1


while second_area > 0:
    # Delete all possible "X" from allowed_cells. Delete possible forbidden cells
    to_delete = []
    print("forbidden_cells", forbidden_cells)
    for i in range(len(forbidden_cells)):
        if forbidden_cells[i] == ["X"]:
            to_delete.append(forbidden_cells[i])
        if forbidden_cells[i] in allowed_cells and forbidden_cells[i] != ["X"]:

            to_delete.append(forbidden_cells[i])
    for i in to_delete:
        print("to delete: ", to_delete,i)
        ind = forbidden_cells.index(i)
        print("ind", ind)
        del forbidden_cells[ind]

    # Random cell to place next tile
    new_cell_num = random.randint(0, len(forbidden_cells)-1)
    new_cell = forbidden_cells[new_cell_num]
    # Replace with "X" and delete it from allowed_cells
    game_field[new_cell[0]][new_cell[1]] = ["X"]
    del forbidden_cells[new_cell_num]
    # Add new cells to allowed_cells
    cells_around(new_cell[0], new_cell[1], width, height, forbidden_cells)
    second_area -= 1

print(two_continent_area)

for i in range(height):
    print(game_field[i])
