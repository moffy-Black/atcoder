#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    A_list = list(map(int, lines[1].split()))
    minus_cnt = 0
    for i in range(N):
        a = A_list[i]
        if a < 0:
            minus_cnt += 1
            A_list[i] = -a

    ans = sum(A_list)
    if minus_cnt % 2 == 0:
        print(ans)
    else:
        print(ans-min(A_list)*2)