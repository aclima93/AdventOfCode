
import sys
import hashlib

input_file = open(sys.argv[1])
input_lines = input_file.readlines()

vowels = "aeiou"
forbidden_patterns = ["ab", "cd", "pq", "xy"]
nice_strings = 0

for line in input_lines:

    word = line.lstrip().rstrip()

    # count vowels
    vowel_counter = 0
    for vowel in vowels:
        vowel_counter += word.count(vowel)

    # check for repeatitions
    repetitions_counter = 0
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            repetitions_counter += 1

    # check for forbidden patterns
    forbidden_patterns_counter = 0
    for forbidden_pattern in forbidden_patterns:
        forbidden_patterns_counter += word.count(forbidden_pattern)

    if (vowel_counter >= 3) and (repetitions_counter >= 1) and (forbidden_patterns_counter == 0):
        nice_strings += 1
        print(word)

print(nice_strings)