#!/usr/bin/env python3

def main(filename):
    freq = 0
    with open(filename) as f:
        for line in f.readlines():
            change = int(line)
            freq += change
    print('Resulting frequency: {}'.format(freq))

def main2(filename):
    freq = 0
    freq_history = {0: True}
    while True:
        with open(filename) as f:
            for line in f.readlines():
                change = int(line)
                freq += change
                if freq not in freq_history:
                    freq_history[freq] = True
                else:
                    print('Found first repeated frequency: {}'.format(freq))
                    return

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Need filename to run')
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)
    main2(filename)
