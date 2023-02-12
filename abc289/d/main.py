#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    a_list = list(map(int, lines[1].split()))
    M = int(lines[2])
    b_list = list(map(int, lines[3].split()))
    X = int(lines[4])

    dp = [0 for _ in range(X+1)];dp[0]=1
    for b in b_list:
        dp[b]=-1

    for i in range(X+1):
        if dp[i] == 1:
            for a in a_list:
                try:
                    if dp[i+a] == 0:
                        dp[i+a] = 1
                except:
                    pass
    if dp[X]:
        print("Yes")
    else:
        print("No")