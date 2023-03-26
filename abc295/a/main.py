#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    w = [x for x in lines[1].split()]

    for i in range(N):
        if w[i] in ["and", "not", "that", "the", "you"]:
            print("Yes")
            break
    else:
        print("No")
