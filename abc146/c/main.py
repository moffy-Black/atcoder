#!/opt/homebrew/bin/python
import sys
import math

def clac_d(N):
    return N // 10 + 1

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    A,B,X = map(int, lines[0].split())

    for i in range(10,0,-1):
        right = B*i
        left = X - right
        estimate_N = left // A
        if estimate_N >= 10**(i-1):
            if estimate_N > 10**9:
                print(10**9)
            else:
                if i != len(str(estimate_N)): #割り切った結果桁数が{i}よりも一つ大きい数値になることがある
                    print(estimate_N-1)
                else:
                    print(estimate_N)
            break
    else:
        print(0)
