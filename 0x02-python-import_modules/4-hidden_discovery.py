#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    arr = dir()
    for name in arr:
        if not name.startswith("__"):
            print(name)
