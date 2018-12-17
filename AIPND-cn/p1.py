env_data = [[3, 2, 2, 2, 2, 2, 2, 2, 1], [0, 0, 2, 2, 2, 2, 2, 0, 0], [
    2, 0, 0, 2, 2, 2, 0, 0, 2], [2, 2, 0, 0, 2, 0, 0, 2, 2], [2, 2, 2, 0, 0, 0, 2, 2, 2]]

# # [[3, 2, 2, 2, 2, 2, 2, 2, 1],
# #  [0, 0, 2, 2, 2, 2, 2, 0, 0],
# #  [2, 0, 0, 2, 2, 2, 0, 0, 2],
# #  [2, 2, 0, 0, 2, 0, 0, 2, 2],
# #  [2, 2, 2, 0, 0, 0, 2, 2, 2]]
def is_move_valid_special(env_data,loc, act):
    tar_value = None


    rows = len(env_data) - 1
    columns = len(env_data[0]) - 1
    env_data.append([1,2,3,4,5,6,7,8,9])
    print(env_data)

    directionDict = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}
    target_pot = (directionDict[act][0]+loc[0], directionDict[act][1]+loc[1])

    tar_x, tar_y = target_pot

    if tar_x < 0 or tar_x > rows or tar_y < 0 or tar_y > columns:
        tar_value == None
    else:
        tar_value = env_data[tar_x][tar_y]

    print(tar_value)
    if tar_value == 2:
        return False
    if tar_value == None:
        return False
    else:
        return True

loc_map = {"start":(0,8), "destination":(0,0)}
robot_current_loc = loc_map["start"]
print(is_move_valid_special(env_data, robot_current_loc, "d"))
print(env_data)
