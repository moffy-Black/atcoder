#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,M = map(int, lines[0].split())
    S_list = lines[1:]
    ans = 0
    for i in range(N):
        a_list = S_list[i]
        for j in range(i+1,N):
            b_list = S_list[j]
            for k in range(M):
                a = a_list[k];b=b_list[k]
                if a=="o" or b=="o":
                    continue
                else:
                    break
            else:
                ans += 1
    print(ans)


