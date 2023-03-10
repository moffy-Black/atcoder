#!/opt/homebrew/bin/python
import sys
import bisect

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,M = map(int,lines[0].split())
    A = sorted(list(map(int,lines[1].split())))

    for _ in range(M):
        bisect.insort(A,(A[-1]/2))
        A.pop()

    ans = sum(list(map(int,A)))

    print(ans)