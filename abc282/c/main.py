#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    S = list(lines[1])
    include = False
    for i in range(N):
        s = S[i]
        if not include:
            if s == ',':
                S[i] = "."
            elif s == '"':
                include = True
        else:
            if s == '"':
                include = False
    for s in S:
        print(s,end="")
    print()