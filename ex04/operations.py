#!/usr/bin/env python3
from sys import argv

usage = 'Usage: python operations.py <number1> <number2>\
\nExample:\n\tpython operations.py 10 3'
if __name__ == "__main__":
    if (len(argv) > 3):
        print('InputError: too many arguments\n')
        print(usage)
    elif (len(argv) < 3):
        print(usage)
    else:
        try:
            n1 = int(argv[1])
            n2 = int(argv[2])
            print(f'Sum:\t\t{n1 + n2}')
            print(f'Difference:\t{n1 - n2}')
            print(f'Product:\t{n1 * n2}')
            print('Quotient:\t', end='')
            if (n2):
                print(n1 / n2)
            else:
                print('ERROR (div by zero)')
            print('Remainder:\t', end='')
            if (n2):
                print(n1 % n2)
            else:
                print('ERROR (modulo by zero)')
        except ValueError:
            print('InputError: only numbers\n')
            print(usage)
