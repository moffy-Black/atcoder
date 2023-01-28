#!/opt/homebrew/bin/python
import sys

def is_nbit(b,n):
    if b & (1<<n):
        return 1
    return 0

def extract_case(N,M,p_list,bulb_requirements):
    ans = 0
    for i in range(2**N):
        for j in range(len(p_list)):
            p = p_list[j];req = bulb_requirements[j]
            cnt = 0
            for k in req[1:]:
                cnt += is_nbit(i,k-1)
            if cnt % 2 == p:
                continue
            else:
                break
        else:
            ans += 1
    return ans



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))

    N,M = map(int,lines[0].split())
    bulb_requirements = []
    for line in lines[1:M+1]:
        bulb_requirements.append(list(map(int,line.split())))
    p_list = list(map(int,lines[M+1].split()))

    print(extract_case(N,M,p_list,bulb_requirements))
