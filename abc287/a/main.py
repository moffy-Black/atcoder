#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    against = 0
    for line in lines[1:]:
        if line == "Against":
            against += 1
    if N-against >= against:
        print("Yes")
    else:
        print("No")