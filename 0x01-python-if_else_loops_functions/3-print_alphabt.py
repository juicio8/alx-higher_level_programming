#!/usr/bin/python3
for alpha in range(97, 97 + 26):
    if chr(alpha) == 'q' or chr(alpha) == 'e':
        continue
    else:
        print("{}".format(chr(alpha)), end='')
