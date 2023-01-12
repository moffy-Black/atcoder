#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    S = lines[0]
    ans = 0
    duplicate = False
    for s in S:
        if duplicate:
            if s != "0":
                ans += 1
            duplicate = False
        else:
            if s == "0":
                duplicate = True
            ans += 1
    print(ans)
