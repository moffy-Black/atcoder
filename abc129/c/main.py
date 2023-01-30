#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,M = map(int,lines[0].split())
    a_set = set(map(int,lines[1:]))
    case_list = [0 for _ in range(N)]
    if N < 2:
        print(1)
    else:
        if 1 in a_set and 2 in a_set:
            case_list[0]=0;case_list[1]=0
        elif 1 in a_set:
            case_list[0]=0;case_list[1]=1
        elif 2 in a_set:
            case_list[0]=1;case_list[1]=0
        else:
            case_list[0]=1;case_list[1]=2
        for i in range(2,N):
            if i+1 not in a_set:
                case_list[i]=case_list[i-1]+case_list[i-2]
        print(case_list[-1] % 1000000007)