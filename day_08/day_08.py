import sys

if __name__ == "__main__":

    input_file = open(sys.argv[1])
    input_lines = input_file.readlines()

    num_in_memory = 0
    num_in_string = 0

    for line in input_lines:
        # ignore whitespace
        line = line.lstrip().rstrip()

        # number of literals in string is its length
        num_in_string += len(line)

        # detect escaped characters
        in_memory_line = bytes(line, "utf-8").decode("unicode_escape")

        # remove delimiting quotation marks at beginning and end
        in_memory_line = in_memory_line[1:-1]

        num_in_memory += len(in_memory_line)

        print(line)
        print(in_memory_line)

    print(num_in_string - num_in_memory)
