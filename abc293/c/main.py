#!/opt/homebrew/bin/python
import sys

def DFS(node,path,square,dp):
    h,w = node
    a = square[h][w]
    memo_path = path.copy()
    if not a in memo_path:
        memo_path.add(a);dp[h][w] += 1
        if h+1 < len(square):
            DFS((h+1,w),memo_path,square,dp)
        if w+1 < len(square[0]):
            DFS((h,w+1),memo_path,square,dp)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    H,W = map(int, lines[0].split())
    square = [];dp = [[0]*W for _ in range(H)]
    for line in lines[1:]:
        square.append(list(map(int, line.split())))

    DFS((0,0),set(),square,dp)
    print(dp[-1][-1])