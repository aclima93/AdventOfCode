
import sys
import hashlib

input_file = open(sys.argv[1])
input_lines = input_file.readlines()

# populate lights
lights = []
for i in range(1000):
    lights.append( [False] * 1000 )

for line in input_lines:
    instruction = line.lstrip().rstrip()

    left, right = instruction.split("through")

    left = left.lstrip().rstrip()
    if "turn off" in left:
        value = False
        left = left[len("turn off"):]
    elif "turn on" in left:
        value = True
        left = left[len("turn on"):]
    else:
        value = "toggle"
        left = left[len("toggle"):]

    min_i, min_j = left.lstrip().rstrip().split(",")
    max_i, max_j = right.lstrip().rstrip().split(",")
    min_i = int(min_i)
    min_j = int(min_j)
    max_i = int(max_i)
    max_j = int(max_j)

    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if value == "toggle":
                lights[i][j] = (not lights[i][j])
            else:
                lights[i][j] = value

# count lit lights
lit_lights = 0
for lights_row in lights:
    lit_lights += lights_row.count(True)
print(lit_lights)