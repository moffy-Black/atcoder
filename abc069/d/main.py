#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    H,W = map(int, lines[0].split(' '))
    N = int(lines[1])
    A = list(map(int, lines[2].split(' ')))
    ans = [[0]*W for _ in range(H)]
    color_num = 1;color_change_flag = 0
    for i in range(H):
        if i % 2:
            for j in range(W-1, -1, -1):
                ans[i][j] = color_num
                A[color_change_flag] -= 1
                if A[color_change_flag] == 0:
                    color_change_flag += 1
                    color_num += 1

        else:
            for j in range(W):
                ans[i][j] = color_num
                A[color_change_flag] -= 1
                if A[color_change_flag] == 0:
                    color_change_flag += 1
                    color_num += 1

    for i in range(H):
        print(' '.join(map(str, ans[i])))
