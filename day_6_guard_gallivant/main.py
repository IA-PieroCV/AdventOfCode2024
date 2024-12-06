with open("input.txt", "r") as file:
    maze_text = file.read()

z = maze_text.replace("\n", "").index("^")
maze = maze_text.split("\n")
row, column = z // len(maze[-1]), z % len(maze[-1])

ending = False
facing = "up"

coords = set()
final_positions = set()

while not ending:
    if facing == "up":
        last_index = -1
        traj_with_obstacles = [maze[i][column] for i in range(row, last_index, -1)]  #
        if "#" in traj_with_obstacles:
            last_index = row - traj_with_obstacles.index("#")  #
        else:
            ending = True
        _ = [coords.add((i, column)) for i in range(row, last_index, -1)]  #
        row = last_index + 1
        facing = "right"
    elif facing == "right":
        last_index = len(maze[row])
        traj_with_obstacles = maze[row][column:]  #
        if "#" in traj_with_obstacles:
            last_index = column + traj_with_obstacles.index("#")  #
        else:
            ending = True
        _ = [coords.add((row, j)) for j in range(column, last_index)]  #
        column = last_index - 1  #
        facing = "down"
    elif facing == "down":
        last_index = len(maze)
        traj_with_obstacles = [maze[i][column] for i in range(row, last_index)]  #
        if "#" in traj_with_obstacles:
            last_index = row + traj_with_obstacles.index("#")  #
        else:
            ending = True
        _ = [coords.add((i, column)) for i in range(row, last_index)]  #
        row = last_index - 1  #
        facing = "left"
    elif facing == "left":
        last_index = -1
        traj_with_obstacles = maze[row][column::-1]  #
        if "#" in traj_with_obstacles:
            last_index = column - traj_with_obstacles.index("#")  #
        else:
            ending = True
        _ = [coords.add((row, j)) for j in range(column, last_index, -1)]  #
        column = last_index + 1  #
        facing = "up"

    if (row, column) in final_positions:
        ending = True
    final_position = (row, column)
    final_positions.add(final_position)

print("PART 1:", len(coords))

total_loops = 0
row, column = z // len(maze[-1]), z % len(maze[-1])
for coord in coords - {(row, column)}:
    maze_temp = maze[::]
    maze_temp[coord[0]] = (
        maze_temp[coord[0]][: coord[1]] + "#" + maze_temp[coord[0]][coord[1] + 1 :]
    )

    row, column = z // len(maze[-1]), z % len(maze[-1])
    ending = False
    facing = "up"
    final_positions = set()

    while not ending:
        just_turning = False
        if facing == "up":
            last_index = -1
            traj_with_obstacles = [
                maze_temp[i][column] for i in range(row, last_index, -1)
            ]  #
            if "#" in traj_with_obstacles:
                last_index = row - traj_with_obstacles.index("#")  #
            else:
                ending = True
            just_turning = row == last_index + 1
            row = last_index + 1
            facing = "right"
        elif facing == "right":
            last_index = len(maze_temp[row])
            traj_with_obstacles = maze_temp[row][column:]  #
            if "#" in traj_with_obstacles:
                last_index = column + traj_with_obstacles.index("#")  #
            else:
                ending = True
            just_turning = column == last_index - 1
            column = last_index - 1  #
            facing = "down"
        elif facing == "down":
            last_index = len(maze_temp)
            traj_with_obstacles = [
                maze_temp[i][column] for i in range(row, last_index)
            ]  #
            if "#" in traj_with_obstacles:
                last_index = row + traj_with_obstacles.index("#")  #
            else:
                ending = True
            just_turning = row == last_index - 1
            row = last_index - 1  #
            facing = "left"
        elif facing == "left":
            last_index = -1
            traj_with_obstacles = maze_temp[row][column::-1]  #
            if "#" in traj_with_obstacles:
                last_index = column - traj_with_obstacles.index("#")  #
            else:
                ending = True
            just_turning = column == last_index + 1
            column = last_index + 1  #
            facing = "up"

        if (row, column) in final_positions and not just_turning:
            total_loops += 1
            ending = True
        final_position = (row, column)
        final_positions.add(final_position)

print("PART 2:", total_loops)
