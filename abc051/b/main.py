#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    K,S = map(int,lines[0].split())
    ans = 0
    for x in range(K+1):
        for y in range(K+1):
            z = S-(x+y)
            if z > K:
                continue
            elif z < 0:
                break
            ans += 1
    print(ans)