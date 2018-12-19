#!/usr/bin/env python3


def letter_frequency(s):
    letter_dict = {}
    for c in s:
        if c not in letter_dict:
            letter_dict[c] = 1
        else:
            letter_dict[c] += 1
    return letter_dict

def has_two_letters(s):
    return 2 in letter_frequency(s).values()

def has_three_letters(s):
    return 3 in letter_frequency(s).values()

def part1(ids):
    twos = 0
    threes = 0
    for _id in ids:
        if has_two_letters(_id):
            twos += 1
        if has_three_letters(_id):
            threes += 1
    print('Checksum: {}'.format(twos*threes))


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Needs filename")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        data = f.readlines()
        part1(data)

