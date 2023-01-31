#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N=int(lines[0])
    sum_dict = dict()
    tmp_sum = 0
    for i in range(1,N+1):
        tmp_sum+=i
        if tmp_sum >= N:
            ans=set([*range(1,i+1)])
            if tmp_sum != N:
                ans.remove(tmp_sum-N)
                break
    for a in ans:
        print(a)