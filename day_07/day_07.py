
import sys

input_file = open(sys.argv[1])
input_lines = input_file.readlines()

wires = {}

for line in input_lines:
    # split the instruciton
    instruction = line.lstrip().rstrip()
    instruction_parts = instruction.split(" ")
    instruction_parts.remove("->")

    # determine type of instruction
    num_parts = len(instruction_parts)

    # assignment instruction (123 -> x)
    if num_parts == 2:
        value = instruction_parts[0]
        target_label = instruction_parts[1]
        wires[target_label] = int(value)

    # negated assignment (NOT y -> x)
    elif num_parts == 3:
        source_label = instruction_parts[1]
        target_label = instruction_parts[2]
        value = wires[source_label]
        wires[target_label] = (~ value)

    # two label operations
    else:
        left_source = instruction_parts[0]
        operation = instruction_parts[1]
        right_source = instruction_parts[2]
        target_label = instruction_parts[3]

        try:
            left_value = int(left_source)
        except ValueError:
            left_value = wires[left_source]

        try:
            right_value = int(right_source)
        except ValueError:
            right_value = wires[right_source]

        if operation == "AND":
            value = left_value & right_value
        elif operation == "OR":
            value = left_value | right_value
        elif operation == "LSHIFT":
            value = left_value << right_value
        elif operation == "RSHIFT":
            value = left_value >> right_value

print(wires)
print(wires["a"])
