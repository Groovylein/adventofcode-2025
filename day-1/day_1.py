def rotate(initial_number, dail_rotation):
    direction = dail_rotation[0]
    rot_num = int(dail_rotation[1:])
    new_number = initial_number
    if direction == 'L':
        new_number = initial_number - rot_num
        if new_number < 0 :
            new_number = new_number + 100
    elif direction == 'R':
        if new_number > 100 :
            new_number = new_number - 100
    
    return new_number