
import sys
import hashlib

input_file = open(sys.argv[1])
input_lines = input_file.readlines()


for line in input_lines:

    private_key = line.lstrip().rstrip()
    counter = 1
    magic_number_1st_half = -1
    magic_number_2nd_half = -1
    adventcoin = private_key + str(counter)

    while True:
        digest = hashlib.md5(adventcoin.encode('utf-8')).hexdigest()

        # 1st half
        if (magic_number_1st_half == -1) and (digest[0:5] == "00000"):
            magic_number_1st_half = counter

        # 2nd half
        if (magic_number_2nd_half == -1) and (digest[0:6] == "000000"):
            magic_number_2nd_half = counter

        # both solutions have been found
        if (magic_number_1st_half != -1) and (magic_number_2nd_half != -1):
            break
        else:
            counter += 1
            adventcoin = private_key + str(counter)

    print(magic_number_1st_half, magic_number_2nd_half)

