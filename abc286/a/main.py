#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,P,Q,R,S = map(int, lines[0].split())
    a_list = list(map(int, lines[1].split()))
    for i in range(Q-P+1):
        a_list[P+i-1],a_list[R+i-1] = a_list[R+i-1], a_list[P+i-1]
    print(*a_list)