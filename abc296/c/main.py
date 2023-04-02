#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,X = map(int, lines[0].split())
    A = list(map(int, lines[1].split()))

    A_set = set()
    for i in range(N):
        a = A[i]
        A_set.add(a)

    for i in range(N):
        ai = A[i]
        aj = ai - X
        if aj in A_set:
            print("Yes")
            break
    else: print("No")