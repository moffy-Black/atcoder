#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    S = lines[0]
    for i in range(len(S)):
        if S[i].islower():
            pass
        else:
            print(i+1)
            break