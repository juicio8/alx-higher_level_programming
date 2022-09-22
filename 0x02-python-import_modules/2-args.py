#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    lists = sys.argv
    length = len(sys.argv) - 1
    arg = "argument"
    print("{} argument{}{}".format(length, " " if length == 1 else "s", "." if length == 0 else ":"))
    for i in range(1, len(lists)):
        print("{}: {}".format(i, lists[i])) 
