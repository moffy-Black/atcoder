#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0]);ans = N
    right_left_list = []
    for i in range(1,N+1):
        x,l = map(int,lines[i].split())
        left,right = x-l,x+l
        right_left_list.append([right,left])
    right_left_list = sorted(right_left_list)

    ans = N;r,l = 0,1
    while l < N:
        right,left = right_left_list[r][0],right_left_list[l][1]
        if right > left:
            ans -= 1
            l+=1
        else:
            r+=l-r;l+=1

    print(ans)