
import sys

def update_deliveries(houses, x, y):

    if (x, y) not in houses:
        houses[(x, y)] = 1

    return houses

def update_position(direction, x, y):
    if direction == '^':
        y += 1

    elif direction == 'v':
        y -= 1

    elif direction == '>':
        x += 1

    elif direction == '<':
        x -= 1

    return x, y

if __name__ == "__main__":

    input_file = open(sys.argv[1])
    input_lines = input_file.readlines()

    for line in input_lines:
        start_x = 0
        start_y = 0
        deliveries = {(start_x, start_y): 1}

        santa_start_x = 0
        santa_start_y = 0
        robo_start_x = 0
        robo_start_y = 0
        santa_and_robo_deliveries = {(robo_start_x, robo_start_y): 1}

        char_index = 0
        for char in line:

            # # 1st half
            # update position
            start_x, start_y = update_position(char, start_x, start_y)

            # update present distribution
            deliveries = update_deliveries(deliveries, start_x, start_y)

            # # 2nd half
            # santa's turn
            if char_index % 2 == 0:

                # update position
                santa_start_x, santa_start_y = update_position(char, santa_start_x, santa_start_y)

                # update present distribution
                santa_and_robo_deliveries = update_deliveries(santa_and_robo_deliveries, santa_start_x, santa_start_y)

            # robo santa's turn
            else:

                # update position
                robo_start_x, robo_start_y = update_position(char, robo_start_x, robo_start_y)

                # update present distribution
                santa_and_robo_deliveries = update_deliveries(santa_and_robo_deliveries, robo_start_x, robo_start_y)

            char_index += 1

        print("\n", line)

        # 1st half
        print("deliveries", sum(deliveries.values()) )

        # 2nd half
        print("santa_and_robo_deliveries", sum(santa_and_robo_deliveries.values()))
