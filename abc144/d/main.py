#!/opt/homebrew/bin/python
import sys
import math

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    a,b,x = map(int, lines[0].split())
    youryou = a*a*b
    if youryou/2 < x:
        h = (youryou-x) / (a**2) * 2
        c = (a**2+h**2)**0.5
        theta =math.asin(h/c) * 180 / math.pi
        print(theta)
    else:
        h = x / (a*b) * 2
        c = (b**2+h**2)**0.5
        theta = math.asin(h/c) * 180 / math.pi
        print(90-theta)
