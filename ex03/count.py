#!/usr/bin/env python3
from string import punctuation


def text_analyzer(*args):
    '''This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.'''
    if len(args) > 1:
        print('ERROR')
        exit(1)
    if not args:
        text = input('What is the text to analyse?\n>> ')
    else:
        text = args[0]
    length = len(text)
    n_upper = 0
    n_lower = 0
    n_punc = 0
    n_space = 0
    print(f'The text contains {length} characters:')
    if length:
        n_space = text.count(' ')
        n_upper = len(list(filter(lambda x: x.isupper(), text)))
        n_lower = len(list(filter(lambda x: x.islower(), text)))
        n_punc = len(list(filter(lambda x: x in punctuation, text)))
    print(f'- {n_upper} upper letters')
    print(f'- {n_lower} lower letters')
    print(f'- {n_punc} punctuation marks')
    print(f'- {n_space} spaces')
