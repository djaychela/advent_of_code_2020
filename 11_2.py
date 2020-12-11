import pathlib
import copy

file_name = "11.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    seating = [list(seat_row.strip()) for seat_row in file.readlines()]

cols = len(seating[0])
rows = len(seating)
changes = True
runs = 1

def display_seating(seat_array):
    score = 0
    for row in seat_array:
        for seat in row:
            print(seat, end='')
            if seat == "#":
                score += 1
        print()
    return score

while changes:
    changes = False
    previous = copy.deepcopy(seating)
    for row in range(rows):
        for col in range(cols):
            if previous[row][col] != ".":
                occupied = 0
                directions = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1, 0), (1, -1)]
                for direction in directions:
                    search_position = [row, col]
                    searching = True
                    while searching:
                        search_position[0] += direction[0]
                        search_position[1] += direction[1]
                        if 0 > search_position[0]:
                            searching = False
                        if search_position[0] >= rows:
                            searching = False
                        if 0 > search_position[1]:
                            searching = False
                        if search_position[1] >= cols:
                            searching = False
                        if searching:
                            if previous[search_position[0]][search_position[1]] == "#":
                                if search_position[0] == row and search_position[1] == col:
                                    pass
                                else:
                                    occupied += 1
                                    searching = False
                            if previous[search_position[0]][search_position[1]] == "L":
                                searching = False
                
                if previous[row][col] == "L" and occupied == 0:
                    seating[row][col] = "#"
                    changes = True
                if previous[row][col] == "#" and occupied >= 5:
                    seating[row][col] = "L"
                    changes = True

    score = display_seating(seating)
    print(f"Run {runs} complete. Score = {score}")
    runs += 1


