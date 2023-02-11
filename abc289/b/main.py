#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,M = map(int,lines[0].split())
    a_list = list(map(int, lines[1].split()));a_set = set(a_list)
    moji_set = {i for i in range(1,N+1)}
    ans = []
    def recr(n):
        if n in a_set:
            return recr(n+1)
        else:
            return n
    i = 1
    while True:
        if i > N:
            break
        tmp = recr(i)
        ans+=[i for i in range(tmp,i-1,-1)]
        i = tmp+1
    print(" ".join(list(map(str,ans))))

