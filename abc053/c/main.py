#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    x = int(lines[0])
    bit = 0
    amari = x%11
    if amari == 0:
        bit = 0
    elif amari > 6:
        bit = 2
    else:
        bit = 1
    ans = 2*(x//11) + bit
    print(ans)
