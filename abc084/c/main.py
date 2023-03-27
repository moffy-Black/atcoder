#!/opt/homebrew/bin/python
import sys
sys.setrecursionlimit(10**6)

def recr_train(i,t,csf_list,N):
    if i == N-1:
        return t
    else:
        c, s, f = csf_list[i]
        if t == 0:
            return recr_train(i+1, c+s, csf_list, N)
        else:
            if t <= s:
                wait_time = s - t
            else:
                dis_time = t - s
                if dis_time % f == 0:
                    wait_time = 0
                else:
                    wait_time = f - (dis_time % f)
            return recr_train(i+1, t+wait_time+c, csf_list, N)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))

    N = int(lines[0]);csf_list = []
    for line in lines[1:]:
        csf_list.append(list(map(int, line.split())))

    for i in range(N):
        print(recr_train(i,0,csf_list,N))
