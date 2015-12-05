
import sys

input_file = open(sys.argv[1])
input_lines = input_file.readlines()


for line in input_lines:
    start_x = 0
    start_y = 0
    deliveries = {(start_x, start_y):1}

    for char in line:

        # update position
        if char == '^':
            start_y += 1

        elif char == 'v':
            start_y -= 1

        elif char == '>':
            start_x += 1

        elif char == '<':
            start_x -= 1

        # update present distribution
        if (start_x, start_y) not in deliveries:
            deliveries[(start_x, start_y)] = 1

    print( sum(deliveries.values()) )