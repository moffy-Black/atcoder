#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    S = lines[1]

    tmp = S[0]
    for s in S[1:]:
        if s == tmp:
            print("No")
            break
        tmp = s
    else:
        print("Yes")