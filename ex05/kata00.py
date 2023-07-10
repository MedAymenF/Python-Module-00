#!/usr/bin/env python3

t = (19, 42, 21)

t = list(map(str, t))
print('The {} numbers are: {}'.format(len(t), ', '.join(t)))
