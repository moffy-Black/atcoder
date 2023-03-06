#!/opt/homebrew/bin/python
import sys
import math

def cnt_pair(n):
    i = 1
    cnt = 0
    while True:
        if i > math.sqrt(n):
            break
        elif i == math.sqrt(n):
            cnt+=1
        elif n % i == 0:
            cnt+=2
        i+=1
    return cnt

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])

    comb_dict = {i:0 for i in range(1,N)}
    for i in range(1,N):
        ab = i;cd = N - ab
        cd_pair_num = cnt_pair(cd)
        comb_dict[cd] = cd_pair_num

    ans = 0
    for i in range(1,N):
        ab = i;cd = N - ab
        ans+=comb_dict[ab]*comb_dict[cd]
    print(ans)
