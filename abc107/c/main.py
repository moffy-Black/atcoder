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
        range_list = X[i:i+K]
        if range_list[0] < 0 and range_list[-1] > 0:
            ans = min(ans, abs(range_list[0])*2+range_list[-1], range_list[-1]*2+abs(range_list[0]))
        else:
            ans = min(ans,max(abs(range_list[0]),range_list[-1]))

    print(ans)