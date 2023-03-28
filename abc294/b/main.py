#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    H,W = map(int, lines[0].split())
    A = []
    for i in range(H):
        A.append(list(map(int, lines[i+1].split())))

    for i in range(H):
        for j in range(W):
            if A[i][j] == 0:
                A[i][j] = "."
            else:
                A[i][j] = chr(A[i][j] + 64)

    for i in range(H):
        print("".join(A[i]))