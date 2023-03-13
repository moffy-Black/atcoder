#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    A = list(map(int, lines[1].split()))
    not_called = {i for i in range(1, N+1)}
    for i in range(N):
        if i+1 not in not_called:
            continue
        if A[i] in not_called:
            not_called.remove(A[i])
    print(len(not_called))
    print(' '.join(map(str, sorted(not_called))))