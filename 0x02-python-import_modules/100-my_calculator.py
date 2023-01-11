#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    n = len(sys.argv)
    operator = ''

    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    x = ord(sys.argv[2])
    if x != 42 and x != 43 and x != 45 and x != 47:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if x == 42:
        operator = '*'
        print("{} {} {} = {}".format(a, operator, b,  mul(a, b))

    if x == 43:
        operator = '+'
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))

    if x == 45:
        operator = '-'
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))

    if x == 47:
        operator = '/'
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
