def next_head(move:str, old_head):
    if move == "up":
        new_head = {"x": old_head["x"], "y": old_head["y"] + 1}
    if move == "down":
        new_head = {"x": old_head["x"], "y": old_head["y"] - 1}
    if move == "left":
        new_head = {"x": old_head["x"] - 1, "y": old_head["y"]}
    if move == "right":
        new_head = {"x": old_head["x"] + 1, "y": old_head["y"]}
    return new_head


def close_to(my_snake, opponent, dis):
    if abs(my_snake["y"]-opponent["y"]) + abs(my_snake["x"] - opponent["x"]) == dis:
        return True
    else:
        return False


# Helper function that prevents snake from colliding with opponents
def avoid_others():
    # TODO
    return


#TODO prevents snake from colliding with itself
def avoid_myself(my_body, is_move_safe):
    return


# TODO prevents snake from colliding with wall
def check_wall(my_head, game_state, is_move_safe):
    return

def find_food():