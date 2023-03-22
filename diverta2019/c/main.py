#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    AB_cnt = 0;top_B_cnt = 0;bottom_A_cnt = 0;both_AB_cnt = 0
    for i in range(N):
        s = lines[i+1]
        for j in range(len(s)-1):
            if s[j] == 'A' and s[j+1] == 'B':
                AB_cnt += 1
        if s[0] == 'B' and s[-1] == 'A':
            both_AB_cnt += 1
        elif s[0] == 'B':
            top_B_cnt += 1
        elif s[-1] == 'A':
            bottom_A_cnt += 1

    attach_list = [top_B_cnt, bottom_A_cnt, both_AB_cnt]
    if both_AB_cnt == 0:
        ans = AB_cnt + min(attach_list[:-1])
    elif sum(attach_list[:-1]) == 0:
        ans = AB_cnt + both_AB_cnt - 1
    else:
        ans = AB_cnt + both_AB_cnt + min(attach_list[:-1])

    print(ans)