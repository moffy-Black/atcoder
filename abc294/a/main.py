#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    A = list(map(int, lines[1].split()))
    ans = []
    for i in range(N):
        if A[i] % 2 == 0:
            ans.append(A[i])
    print(" ".join(map(str, ans)))