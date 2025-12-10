import os
from pathlib import Path, PurePath

def rotate(initial_number, dail_rotation):
    direction = dail_rotation[0]
    rot_num = int(dail_rotation[1:])
    new_number = initial_number
    if direction == 'L':
        new_number = initial_number - rot_num
        while new_number < 0 :
            new_number = new_number + 100
    elif direction == 'R':
        new_number = initial_number + rot_num
        while new_number >= 100 :
            new_number = new_number - 100
    
    return new_number

script_path = Path(__file__)
filename = PurePath(script_path.parent / "input_data_1.txt")
lines = []
with open("C:/Users/kiriakos.antoniadis/GitHub/adventofcode-2025/day-1/input_day_1.txt", 'r') as file:
    file_lines = [line.strip() for line in file]
    

init_num = 50
count_zero = 0
for line in file_lines:
    init_num = rotate(init_num, line)
    print(init_num)
    if init_num == 0:
        count_zero += 1
        
print(f"counted {count_zero} zeros")