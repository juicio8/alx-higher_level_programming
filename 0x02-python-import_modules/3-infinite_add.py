#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lists = sys.argv
    sum = 0
    for i in range(1, len(lists)):
        sum += int(lists[i])
    print(sum)
