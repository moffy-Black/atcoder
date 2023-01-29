#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    S=lines[0];T=lines[1];T_len= len(T)
    front_cnt = 0;back_cnt = 0
    for i in range(T_len):
        if T[i] == S[i] or "?" == S[i] or "?" == T[i]:
            front_cnt+=1
        else:
            break
    for i in range(-1,-1*(T_len)-1,-1):
        if T[i] == S[i] or "?" == S[i] or "?" == T[i]:
            back_cnt+=1
        else:
            break
    ans = []
    for i in range(T_len+1):
        if front_cnt >= i and back_cnt >= T_len-i:
            ans.append("Yes")
        else:
            ans.append("No")
    for a in ans:
        print(a)