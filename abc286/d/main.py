#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,X = map(int, lines[0].split())

    coin_dict = dict()
    for line in lines[1:]:
        a,b = map(int, line.split())
        coin_dict[a] = b
    coin_list = list(sorted(coin_dict.items()))
    min_coin = coin_list[0][0];min_coin_num = coin_list[0][1]

    dp = [[0]*51 for _ in range(N)]
    dp[0] = [min_coin*i for i in range(min_coin_num+1)]+dp[0][min_coin_num+1:]
    def calc(N,X,coin_list,dp):
        for i in range(N-1):
            for j in range(50):
                if dp[i][j]!=0:
                    for k in range(coin_list[i+1][0]+1):
                        value = k * coin_list[i+1][0]+dp[i][j]
                        if value == X:
                            return "Yes"
                        elif value < X:
                            dp[i+1][k] = max(dp[i+1][k],value)
        else:
            return "No"
    ans = calc(N,X,coin_list,dp)
    print(ans)