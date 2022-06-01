#!/usr/bin/python3

for k in range(0, 26):
    if k % 2 == 0:
        print("{:c}".format(122 - k), end="")
    else:
        print("{:c}".format(90 - k), end="")
