#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    n = int(lines[0])
    v_list = list(map(int,lines[1].split()))
    odd_dict = dict();even_dict = dict()
    for i in range(0,n-1,2):
        odd_dict.setdefault(v_list[i],0)
        odd_dict[v_list[i]]+=1
    for i in range(1,n,2):
        even_dict.setdefault(v_list[i],0)
        even_dict[v_list[i]]+=1
    odd_dict = sorted([(v,k) for k,v in odd_dict.items()]);even_dict = sorted([(v,k) for k,v in even_dict.items()])
    if odd_dict[-1][1]==even_dict[-1][1]:
        if len(odd_dict) > 1 and len(even_dict) > 1:
            ans = min((n//2 - odd_dict[-1][0]) + (n//2 - even_dict[-2][0]),(n//2 - odd_dict[-2][0]) + (n//2 - even_dict[-1][0]))
        elif len(odd_dict) > 1:
            ans = (n//2 - odd_dict[-2][0]) + (n//2 - even_dict[-1][0])
        elif len(even_dict) > 1:
            ans = (n//2 - odd_dict[-1][0]) + (n//2 - even_dict[-2][0])
        else:
            ans = n//2
    else:
        ans = (n//2 - odd_dict[-1][0]) + (n//2 - even_dict[-1][0])
    print(ans)