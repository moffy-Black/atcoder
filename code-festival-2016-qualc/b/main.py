#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))

    K, T = map(int, lines[0].split())
    A = sorted(list(map(int, lines[1].split())))

    ans = A[-1] - 1 - sum(A[:-1])
    if ans < 0:
        ans = 0
    print(ans)

