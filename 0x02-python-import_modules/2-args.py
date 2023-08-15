#!/usr/bin/python3
import sys

def print_arguments(arguments):
    num = len(arguments)
    if num == 1:
        print(f"{num - 1} argument.")
    else:
        print(f"{num - 1} arguments.")

    for i, arg in enumerate(arguments[1:], start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    arguments = sys.argv
    print_arguments(arguments)
