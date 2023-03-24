#!/opt/homebrew/bin/python
import sys
import bisect


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    A = sorted(list(map(int, lines[1].split(' '))))

    ans = [0, 0]

    a = A[N-1];tmp_A = A[:N-1]+A[N:]
    if a % 2 == 0:
        half_a = a//2
        half_point = bisect.bisect_left(tmp_A, half_a)
        if half_point == 0:
            half_point = 0
        elif half_point == len(tmp_A):
            half_point = len(tmp_A)-1
        else:
            if abs(tmp_A[half_point-1]-half_a) <= abs(tmp_A[half_point]-half_a):
                half_point -= 1
        ans = [a, tmp_A[half_point]]

    else:
        half_a = (a+1)//2
        half_point = bisect.bisect_left(tmp_A, half_a)
        if half_point == 0:
            half_point = 0
        elif half_point == len(tmp_A):
            half_point = len(tmp_A)-1
        else:
            left_min_dis = min(abs(tmp_A[half_point-1]-half_a), abs(tmp_A[half_point-1]-(half_a-1)))
            right_min_dis = min(abs(tmp_A[half_point]-half_a), abs(tmp_A[half_point]-(half_a-1)))
            if left_min_dis <= right_min_dis:
                half_point -= 1
            ans = [a, tmp_A[half_point]]

    print(" ".join(map(str, ans)))
