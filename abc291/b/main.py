#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    x_list = sorted(list(map(int, lines[1].split())))
    print(sum(x_list[N:4*N])/(3*N))
