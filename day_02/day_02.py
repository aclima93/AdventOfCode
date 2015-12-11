
import sys

input_file = open(sys.argv[1])
input_lines = input_file.readlines()

total_wrapping = 0
total_ribbon = 0

for line in input_lines:
    l, w, h = line.split("x")
    l = int(l)
    w = int(w)
    h = int(h)

    dimensions = [l, w, h]
    min_1 = min(dimensions)
    dimensions.remove(min_1)
    min_2 = min(dimensions)

    total_wrapping += (2 * l * w) + (2 * w * h) + (2 * h * l) + (min_1 * min_2)
    total_ribbon += ((min_1 * 2) + (min_2 * 2)) + (l * w * h)

# first half
print("total_wrapping", total_wrapping)

# second half
print("total_ribbon", total_ribbon)
