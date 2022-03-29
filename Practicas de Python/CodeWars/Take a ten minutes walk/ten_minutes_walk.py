def check_trace(walk):
    north, south, east, west= 0,0,0,0
    for i in range(len(walk)):
        if walk[i] == "n":
            north += 1
            south -= 1
        elif walk[i] == "s":
            south += 1
            north -= 1
        elif walk[i] == "w":
            east += 1
            west -= 1
        elif walk[i] == "e":
            west += 1
            east -= 1
        else:
            return -1
    if north == 0 and south == 0  and east == 0 and west == 0:
        return True
    else:
        return False

def is_valid_walk(walk):
    if len(walk)<=10:
        return check_trace(walk)


print(is_valid_walk(['e', 's', 's', 'e', 'w', 'n', 'n', 'w']))
