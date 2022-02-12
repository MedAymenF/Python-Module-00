#!/usr/bin/env python3

from sys import argv
from string import punctuation

if __name__ == "__main__":
    if len(argv) == 3:
        text = argv[1]
        try:
            length = int(argv[2])
            assert length >= 0
        except Exception:
            print('ERROR')
            exit(1)
        result = [word for word in list(map(lambda x: x.strip(punctuation),
                                        text.split())) if len(word) > length]
        print(result)
    else:
        print('ERROR')
        exit(1)
