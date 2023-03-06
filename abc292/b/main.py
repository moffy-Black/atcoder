#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,Q = map(int, lines[0].split())
    outed = dict()
    for line in lines[1:]:
        event, x = map(int, line.split())
        outed.setdefault(x, 0)
        if event == 1:
            outed[x] += 1
        elif event == 2:
            outed[x] += 2
        else:
            if outed[x] >= 2:
                print('Yes')
            else:
                print('No')