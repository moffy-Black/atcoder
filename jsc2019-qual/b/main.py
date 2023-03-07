#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,K = map(int, lines[0].split())
    A_list = list(map(int, lines[1].split()))
    MOD=10**9+7;ans = 0
    cnt = [0 for _ in range(2*N)]

    A_list *= 2
    for i in range(2*N):
        for j in range(i+1,2*N):
            if A_list[i] > A_list[j]:
                cnt[i] += 1

    root = sum(cnt[N:]);multi = (K*(K+1)//2) % MOD
    difference = sum(cnt[:N]) - (2 * root)
    root_part = (root * multi % MOD);difference_part = (difference * (K*(K-1)//2) % MOD)
    ans =  root_part + difference_part
    print(ans % MOD)