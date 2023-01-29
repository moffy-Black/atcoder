#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,M = map(int,lines[0].split())
    cnt = 0
    t_set = {t for t in lines[N+1:]}
    for s in lines[1:N+1]:
        if s[-3:] in t_set:
            cnt += 1

    print(cnt)

