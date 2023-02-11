#!/opt/homebrew/bin/python
import sys
import itertools

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,M = map(int, lines[0].split())
    c_list = [];a_list = []
    for i in range(1,2*M+1):
        if i % 2 == 1:
            c = int(lines[i])
            c_list.append(c)
        else:
            a=list(map(int,lines[i].split()))
            a_list.append(a)


    ans = 0
    for i in range(1,M+1):
        tmp=set()

        for v in itertools.combinations(a_list,i):
            tmp|=set([ flatten for inner in list(v) for flatten in inner ])
            if len(tmp)==N:
                ans+=1
            tmp = set()

    print(ans)