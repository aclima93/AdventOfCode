
import sys

input_file = open(sys.argv[1])
input_lines = input_file.readlines()

for line in input_lines:

    starting_floor = 0
    final_floor = starting_floor

    for char in line:
        if char == '(':
            final_floor += 1
        elif char == ')':
            final_floor -= 1

    print(final_floor)
