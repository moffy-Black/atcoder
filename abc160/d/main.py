#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,X,Y = map(int, lines[0].split());X-=1;Y-=1
    cnt_dict = {i:0 for i in range(1,N)}
    for i in range(N):
        for j in range(i+1,N):
            d = min(j-i, abs(X-i)+abs(Y-j)+1)
            cnt_dict[d] += 1
    for i in range(1,N):
        print(cnt_dict[i])