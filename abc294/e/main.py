#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    L,N,M = map(int, lines[0].split())
    upper_list = [];lower_list = []
    for i in range(1,N+1):
        v,l = map(int, lines[i].split())
        upper_list.append([v,l])
    for i in range(N+1,N+M+1):
        v,l = map(int, lines[i].split())
        lower_list.append([v,l])

    ans = 0
    upper_pointer = 0;lower_pointer = 0
    while True:
        if upper_pointer == N and lower_pointer == M:
            break
        upper_vl = upper_list[upper_pointer]
        lower_vl = lower_list[lower_pointer]
        overlap_range = min(upper_vl[1],lower_vl[1])
        if upper_vl[0] == lower_vl[0]:
            ans += overlap_range

        upper_vl[1]-=overlap_range;lower_vl[1]-=overlap_range
        if upper_vl[1] == 0:
            upper_pointer+=1
        if lower_vl[1] == 0:
            lower_pointer+=1

    print(ans)