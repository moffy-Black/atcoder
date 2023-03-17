#!/opt/homebrew/bin/python
import sys
import math

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    D_list = list(map(int, lines[1].split()))
    D_cnt = dict();D_set = set()

    d_max = 0
    for i in range(N):
        d = D_list[i]
        d_max = max(d_max, d)
        D_set.add(d)
        D_cnt.setdefault(d, 0)
        D_cnt[d] += 1

    if D_list[0] == 0 and D_cnt[0] == 1:
        ans = 1
        for i in range(d_max-1, 0, -1):
            if i in D_set:
                ans *= D_cnt[i]**D_cnt[i+1] % 998244353
            else:
                print(0)
                exit()
        print(ans % 998244353)
    else:
        print(0)
        exit()
