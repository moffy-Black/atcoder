#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    if N % 2 == 1:
        print(0)
        sys.exit()
    else:
        n_num = N // 2
        ans = 0
        for i in range(36,0,-1):
            base = 5 **i
            ans += (n_num // base)
        print(ans)

