#!/usr/bin/env python3
from sys import argv

if __name__ == "__main__":
    try:
        assert len(argv) <= 2, 'AssertionError:\
 more than one argument is provided'
        if (len(argv) == 2):
            assert argv[1].isnumeric(), 'AssertionError:\
 argument is not integer'
        else:
            exit()
    except AssertionError as e:
        print(e)
        exit()
    n = int(argv[1])
    if (n == 0):
        print('I’m Zero.')
    elif (n % 2):
        print('I’m Odd.')
    else:
        print('I’m Even.')
