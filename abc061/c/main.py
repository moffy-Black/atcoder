#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,K = map(int, lines[0].split())
    a_list=[];b_list=[]
    for line in lines[1:]:
        a,b = map(int,line.split())
        a_list.append(a);b_list.append(b)
    a_b_lists = sorted(zip(a_list,b_list))
    a_list,b_list = zip(*a_b_lists)
    cnt = 0
    for i in range(N):
        cnt += b_list[i]
        if cnt >= K:
            print(a_list[i])
            break
    else:
        print(a_list[i])