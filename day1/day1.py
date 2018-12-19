#!/bin/env python3

def main(filename):
    freq = 0
    with open(filename) as f:
        for line in f.readlines():
            change = int(line)
            freq += change
    print('Resulting frequency: {}'.format(freq))


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Need filename to run')
        sys.exit(1)
    main(sys.argv[1])
