import sys


if __name__ == "__main__":

    input_file = open(sys.argv[1])
    input_lines = input_file.readlines()

    for line in input_lines:

        # ignore whitespace
        line = line.lstrip().rstrip()

        print('line', line)

        number_occurrences = []
        cur_char = line[0]
        cur_char_counter = 0

        for char in line:
            if char == cur_char:
                cur_char_counter += 1
            else:
                # store the previous count
                number_occurrences.append([cur_char_counter, cur_char])

                # start the next count
                cur_char = char
                cur_char_counter = 1

        # store the last count
        number_occurrences.append([cur_char_counter, cur_char])

        print('number_occurrences', number_occurrences)

        resulting_string = ''
        for char_count in number_occurrences:
            resulting_string += str(char_count[0]) + str(char_count[1])

        print('resulting_string', resulting_string, '\n')
