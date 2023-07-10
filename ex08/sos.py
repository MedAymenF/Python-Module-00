#!/usr/bin/env python3

from sys import argv

ALNM = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

if __name__ == "__main__":
    if len(argv) >= 2:
        text = ' '.join(argv[1:])
        text = text.upper()
        words = text.split()
        for word in words:
            if not word.isalnum():
                print('ERROR')
                exit(1)
        for i, word in enumerate(words):
            if (i):
                print(' / ', end='')
            for j, c in enumerate(word):
                if (j):
                    print(' ', end='')
                print(ALNM[c], end='')
        print('')
