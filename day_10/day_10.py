import sys

def say_it(number):

    number_occurrences = []
    cur_char = number[0]
    cur_char_counter = 0

    for char in number:
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

    say_it_result = ''
    for char_count in number_occurrences:
        say_it_result += str(char_count[0]) + str(char_count[1])

    return say_it_result


if __name__ == "__main__":

    input_file = open(sys.argv[1])
    input_lines = input_file.readlines()

    for line in input_lines:

        # ignore whitespace
        number = line.lstrip().rstrip()

        for i in range(40):
            number = say_it(number)

        print("final_result", len(number))

