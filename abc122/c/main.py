#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,Q = map(int,lines[0].split())
    S = lines[1]
    pointer = 0;ac_flag_list = [0 for _ in range(N-1)]
    while True:
        if pointer >= N-1:
            break
        if S[pointer]=="A" and S[pointer+1]=="C":
            ac_flag_list[pointer]=1
            pointer+=2
        else:
            pointer+=1

    ac_cumulative_sum_list = []
    for i in range(N):
        if i == 0:
            ac_cumulative_sum_list.append(0)
        else:
            ac_cumulative_sum_list.append(ac_cumulative_sum_list[i-1]+ac_flag_list[i-1])

    for line in lines[2:]:
        l,r = map(int,line.split())
        part_ac_num = ac_cumulative_sum_list[r-1]-ac_cumulative_sum_list[l-1]
        print(part_ac_num)