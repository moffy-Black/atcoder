#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    S = lines[0];T = lines[1]
    S_str_dict = {};T_str_dict = {}

    for i in range(len(S)):
        s = S[i];t = T[i]
        S_str_dict.setdefault(s,0)
        T_str_dict.setdefault(t,0)
        S_str_dict[s] += 1
        T_str_dict[t] += 1

    S_str_num = sorted(list(S_str_dict.values()));T_str_num = sorted(list(T_str_dict.values()))
    if S_str_num == T_str_num:
        print('Yes')
    else:
        print('No')