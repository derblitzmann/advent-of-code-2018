#!/usr/bin/env python3


def letter_frequency(s):
    letter_dict = {}
    for c in s:
        if c not in letter_dict:
            letter_dict[c] = 1
        else:
            letter_dict[c] += 1
    return letter_dict

def has_two_letters(d):
    return 2 in d.values()

def has_three_letters(d):
    return 3 in d.values()

def part1(ids):
    twos = 0
    threes = 0
    for _id in ids:
        freqs = letter_frequency(_id)
        if has_two_letters(freqs):
            twos += 1
        if has_three_letters(freqs):
            threes += 1
    print('Checksum: {}'.format(twos*threes))

def part2(ids):
    for i in range(len(ids[0])):
        d = {}
        for _id in ids:
            first_half = _id[:i]
            second_half = _id[i+1:]
            mod_id = first_half + second_half
            if mod_id not in d:
                d[mod_id] = True
            else:
                print(mod_id)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Needs filename")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        data = f.readlines()
        part1(data)
        part2(data)

