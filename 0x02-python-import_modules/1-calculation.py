#!/usr/bin/python3

if __name__ == "__main__":
    from calculation_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(add(a, b, add(a, b))))
