
import sys
import numpy as np

# memoizing function
def set_label_value(label, value):
    # guarrantee that it's an unsgned 16-bit
    wire_values[label] = np.array([int(value)], dtype="uint16")[0]

def get_label_value(label):

    if label in wire_values.keys():
        return wire_values[label]

    # handle when a label is a number
    try:
        return np.array([int(label)], dtype="uint16")[0]
    except ValueError:
        pass

    # determine type of instruction
    instruction_parts = wire_graph[label]
    num_parts = len(instruction_parts)

    # assignment instruction ("123 -> x" or "lx -> a")
    if num_parts == 1:
        value = get_label_value(instruction_parts[0])

    # negated assignment ("NOT y -> x")
    elif num_parts == 2:
        value = (~ get_label_value(instruction_parts[1]))

    # two label operations (AND, OR, LSHIFT, RSHIFT)
    else:
        left_source = instruction_parts[0]
        operation = instruction_parts[1]
        right_source = instruction_parts[2]

        left_value = get_label_value(left_source)
        right_value = get_label_value(right_source)

        if operation == "AND":
            value = left_value & right_value
        elif operation == "OR":
            value = left_value | right_value
        elif operation == "LSHIFT":
            value = left_value << right_value
        elif operation == "RSHIFT":
            value = left_value >> right_value
        else:
            value = 0
            print("This should not happen...")

    set_label_value(label, value)
    return value


if __name__ == "__main__":

    input_file = open(sys.argv[1])
    input_lines = input_file.readlines()

    wire_values = {}  # memoizing variable
    wire_graph = {}  # graph of conections

    for line in input_lines:

        # split the instruction
        instruction = line.lstrip().rstrip()
        instruction_parts = instruction.split(" ")
        instruction_parts.remove("->")

        wire_graph[ instruction_parts[-1] ] = instruction_parts[:-1]

        # initial values for netwrok flow are given by "nice" assignments
        num_parts = len(instruction_parts)
        if num_parts == 2:
            try:
                # if it's a number it is fine
                value = np.array([int(instruction_parts[0])], dtype="uint16")[0]
                target_label = instruction_parts[1]
                wire_values[target_label] = value
            except ValueError:
                pass

    # recursive bottom-up search
    print(get_label_value("a"))
