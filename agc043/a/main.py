#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    H,W = map(int, lines[0].split())
    stage = lines[1:];cnt = 0
    dp = [[0 for _ in range(W)] for _ in range(H)];dp[0][0] = 0 if stage[0][0] == "." else 1
    for i in range(1,H):
        if stage[i-1][0] != stage[i][0]:
            dp[i][0] = dp[i-1][0] + 1
        else:
            dp[i][0] = dp[i-1][0]
    for i in range(1,W):
        if stage[0][i-1] != stage[0][i]:
            dp[0][i] = dp[0][i-1] + 1
        else:
            dp[0][i] = dp[0][i-1]
    for i in range(1,H):
        for j in range(1,W):
            H_candidate = dp[i-1][j]+1 if stage[i][j] != stage[i-1][j] else dp[i-1][j]
            W_candidate = dp[i][j-1]+1 if stage[i][j] != stage[i][j-1] else dp[i][j-1]
            dp[i][j] = min(H_candidate,W_candidate)
    else:
        if stage[-1][-1] == "#":
            dp[-1][-1] += 1
    print(dp[-1][-1]//2)
