import sys

def is_valid_password(password):

    # inscreasing straight check
    increasing_straight = False

    for i in range(len(password)-2):
        subsequence = password[i:i+3]

        first = ord(subsequence[0])
        second = ord(subsequence[1])
        third = ord(subsequence[2])

        # we only need one increasing straight sequence
        if (second == first+1) and (third == second+1):
            increasing_straight = True
            break

    # no forbidden letters check
    no_forbidden_letters = False
    forbidden_letters = ['i', 'o', 'l']

    for char in forbidden_letters:
        if char in password:
            no_forbidden_letters = True
            break

    # two non-overlapping pairs
    two_non_overlapping_pairs = False
    pairs = []
    for i in range(len(password)-1):
        subsequence = password[i:i+2]

        if subsequence[0] == subsequence[1]:
            pairs.append(subsequence)

    # get number of unique pairs
    if len(list(set(pairs))) >= 2:
        two_non_overlapping_pairs = True

    if increasing_straight and no_forbidden_letters and two_non_overlapping_pairs:
        return True

    return False

def increment_password(password):

    incremented_password = password[:-1]
    last_char = password[-1]
    if last_char == 'z':
        incremented_password += 'za'
    else:
        incremented_password += chr(ord(last_char) + 1)

    return incremented_password

def next_password(cur_password):

    new_password = increment_password(cur_password)

    while (len(new_password) == 8) and (not is_valid_password(new_password)):
        new_password = increment_password(new_password)

    return new_password


if __name__ == "__main__":

    input_file = open(sys.argv[1])
    input_lines = input_file.readlines()

    for line in input_lines:

        # ignore whitespace
        line = line.lstrip().rstrip()
        print("next_password", next_password(line))

