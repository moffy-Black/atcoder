#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    S = lines[1]
    arrived = {(0,0)}
    now = [0,0]
    for s in S:
        if s == "R":
            now[0] += 1
        elif s == "L":
            now[0] -= 1
        elif s == "U":
            now[1] += 1
        else:
            now[1] -= 1
        if tuple(now) in arrived:
            print("Yes")
            break
        else:
            arrived.add(tuple(now))
    else:
        print("No")