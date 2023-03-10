#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    a,b,x = map(int,lines[0].split())

    till_b_num = b//x+1
    till_a_num = (a-1)//x+1

    if a == 0:
        print(till_b_num)
    else:
        print(till_b_num - till_a_num)