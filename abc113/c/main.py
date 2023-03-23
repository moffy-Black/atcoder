#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,M = map(int, lines[0].split(' '))
    ans_dict = {i:"" for i in range(M)}
    year_dict = {}

    for i in range(1, M+1):
        line = lines[i]
        p,y = map(int, line.split(' '))
        ans_dict[i-1] += str(p).zfill(6)
        year_dict.setdefault(y,[])
        year_dict[y].append(i-1);year_dict[y].append(p)
    sorted_year_dict = dict(sorted(year_dict.items(), key=lambda x:x[0]))

    state_num_dict = {i:1 for i in range(N)}
    for _,ip in sorted_year_dict.items():
        i,p = ip[0],ip[1]-1
        ans_dict[i] += str(state_num_dict[p]).zfill(6)
        state_num_dict[p] += 1

    for i in range(M):
        print(ans_dict[i])