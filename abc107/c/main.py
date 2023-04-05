#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,K = map(int, lines[0].split())
    X = list(map(int, lines[1].split()))

    ans = 10 ** 9
    for i in range(N-K+1):
        left,right = X[i],X[i+K-1]
        if left < 0 and right > 0:
            ans = min(ans, abs(left)*2+right, right*2+abs(left))
        else:
            ans = min(ans,max(abs(left),right))

    print(ans)