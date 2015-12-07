
import sys
import numpy as np

def get_label_value(label):

    # a label must wait to have a value before it is used
    if label not in wires:
        return -1

    try:
        # if it's a number it is fine
        value = int(label)
    except ValueError:
        # if it's a label we have to check its value
        value = wires[label]

    # guarrantee that it's an unsgned 16-bit
    return np.array([value], dtype="uint16")[0]

def set_label_value(label, value):

    # guarrantee that it's an unsgned 16-bit
    wires[label] = np.array([value], dtype="uint16")[0]

if __name__ == "__main__":

    input_file = open(sys.argv[1])
    input_lines = input_file.readlines()

    wires = {}

    for line in input_lines:

        # split the instruction
        instruction = line.lstrip().rstrip()
        instruction_parts = instruction.split(" ")
        instruction_parts.remove("->")

        # determine type of instruction
        num_parts = len(instruction_parts)

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

    print(wires)
    print(wires["a"])