#!/usr/bin/env python3
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        string = ' '.join(argv[1:])
        string = string.swapcase()
        rstring = string[::-1]
        print(rstring)
