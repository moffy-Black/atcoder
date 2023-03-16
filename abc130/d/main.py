#!/opt/homebrew/bin/python
import sys

def cumulative_sum(int_list):
    cumulative_sum_list = [0] * (len(int_list)+1)
    for i in range(len(int_list)):
            cumulative_sum_list[i+1] = cumulative_sum_list[i] + int_list[i]
    return cumulative_sum_list

def slide_window(cumulative_sum_list,target):
    N = len(cumulative_sum_list) - 1;r = 1;cnt = 0
    for l in range(N):
            while True:
                    if r > N:
                            break
                    if cumulative_sum_list[r] - cumulative_sum_list[l] >= target:
                            cnt += N - r + 1
                            break
                    r += 1
    return cnt

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,K = map(int,lines[0].split())
    a_list = list(map(int,lines[1].split()))

    cumulative_sum_list = cumulative_sum(a_list)
    print(slide_window(cumulative_sum_list,K))