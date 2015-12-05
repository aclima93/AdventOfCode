
import sys
import hashlib

input_file = open(sys.argv[1])
input_lines = input_file.readlines()


for line in input_lines:

    private_key = line.lstrip().rstrip()
    magic_number = 1
    adventcoin = private_key + str(magic_number)

    while True:
        digest = hashlib.md5(adventcoin.encode('utf-8')).hexdigest()
        if digest[0:5] == "00000":
            break
        else:
            magic_number += 1
            adventcoin = private_key + str(magic_number)

    print(magic_number)
    '''
    print(private_key)
    print(adventcoin)
    print(adventcoin.encode('utf-8'))
    print(digest)
    '''
