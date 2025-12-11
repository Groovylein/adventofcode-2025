import os
from pathlib import Path, PurePath

init_num = 50
count_zero = 0
count_zero_rotate = 0

def rotate(initial_number, dail_rotation):
    global count_zero_rotate
    direction = dail_rotation[0]
    rot_num = int(dail_rotation[1:])
    new_number = initial_number
    if direction == 'L':
        new_number = initial_number - rot_num
        while new_number < 0 :
            new_number = new_number + 100
            count_zero_rotate +=1
        if initial_number == 0:
                count_zero_rotate -=1
    elif direction == 'R':
        new_number = initial_number + rot_num
        while new_number >= 100 :
            if new_number != 100:
                count_zero_rotate +=1
            new_number = new_number - 100
            
    
    return new_number

script_path = Path(__file__)
filename = PurePath(script_path.parent / "input_data_1.txt")
lines = []
with open("C:/Users/kiriakos.antoniadis/GitHub/adventofcode-2025/day-1/input_day_1.txt", 'r') as file:
    file_lines = [line.strip() for line in file]
    

for line in file_lines:
    init_num = rotate(init_num, line)
    if init_num == 0:
        count_zero += 1
        

print(f"counted {count_zero} zeros part 1")
print(f"counted {(count_zero + count_zero_rotate)} zeros part 2")