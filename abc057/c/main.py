#!/opt/homebrew/bin/python
import sys
import math

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))

    N = int(lines[0])
    r2_N = math.ceil(math.sqrt(N));ans = 0
    for i in range(1, r2_N + 1):
        if N % i == 0:
            ans = max(len(str(i)), len(str(N // i)))
    print(ans)