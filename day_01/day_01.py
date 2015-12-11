
import sys

input_file = open(sys.argv[1])
input_lines = input_file.readlines()

for line in input_lines:

    cur_char_position = 1
    starting_floor = 0
    cur_floor = starting_floor

    for char in line:
        if char == '(':
            cur_floor += 1
        elif char == ')':
            cur_floor -= 1

        # second half of the problem
        if cur_floor == -1:
            print("cur_char_position", cur_char_position)

        cur_char_position += 1

    # first half of the problem
    print("cur_floor", cur_floor)
