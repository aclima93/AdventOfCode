
import sys
import numpy as np

def set_label_value(label, value):

    # guarrantee that it's an unsgned 16-bit
    wire_values[label] = np.array([value], dtype="uint16")[0]

def get_label_value(label):

    # determine type of instruction
    instruction_parts = wire_graph[label]
    num_parts = len(instruction_parts)

    if num_parts == 1:
        try:
            # if it's a number it is fine
            value = int(label)
        except ValueError:
            # if it's a label we have to check its value
            if label in wire_values.keys():
                value = wire_values[label]
            else:
                value = get_label_value(label)

        # guarrantee that it's an unsgned 16-bit
        return np.array([value], dtype="uint16")[0]

    else:

        # assignment instruction (123 -> x)
        if num_parts == 2:
            value = get_label_value(instruction_parts[0])
            target_label = instruction_parts[1]

        # negated assignment (NOT y -> x)
        elif num_parts == 3:
            value = (~ get_label_value(instruction_parts[1]))
            target_label = instruction_parts[2]

        # two label operations (AND, OR, LSHIFT, RSHIFT)
        else:
            left_source = instruction_parts[0]
            operation = instruction_parts[1]
            right_source = instruction_parts[2]
            target_label = instruction_parts[3]

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

        print(value)
        set_label_value(target_label, value)


if __name__ == "__main__":

    input_file = open(sys.argv[1])
    input_lines = input_file.readlines()

    wire_values = {}
    wire_graph = {}

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
                continue

    print(get_label_value("a"))

    print(wire_values)
    print(wire_graph)
