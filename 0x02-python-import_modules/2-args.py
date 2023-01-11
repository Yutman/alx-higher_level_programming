#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv)
    char = 's'
    colon = ':'

    if n == 1:
        colon = '.'


    if n == 2:
        char = ''


    print("{} argument{}{}".format(n - 1, char, colon))


    for i in range(1, n):
        print("{}: {}".format(i, sys.argv[i]))
