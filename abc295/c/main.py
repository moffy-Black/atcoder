#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    A = list(map(int, lines[1].split()))

    A_cnt_dict = dict()
    for i in range(N):
        a = A[i]
        A_cnt_dict.setdefault(a, 0)
        A_cnt_dict[a] += 1

    ans = 0
    for v in A_cnt_dict.values():
        ans += v // 2
    print(ans)