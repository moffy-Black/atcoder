#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0]);ab_list=[]
    for line in lines[1:]:
        a,b = map(int, line.split())
        ab_list.append([a,b])

    dp = [[0,0] for _ in range(N)];dp[0]=[1,1]
    for i in range(N-1):
        for pre in range(2):
            for next in range(2):
                if ab_list[i][pre] != ab_list[i+1][next]:
                    dp[i+1][next] += dp[i][pre] % 998244353
    print(sum(dp[N-1]) % 998244353)
