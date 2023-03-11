#!/opt/homebrew/bin/python
import sys
import bisect

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,M = map(int,lines[0].split())
    A = sorted(list(map(int,lines[1].split())))
    BC_dict = dict()
    for line in lines[2:]:
        B,C = map(int,line.split())
        BC_dict.setdefault(C,0)
        BC_dict[C] += B
    C_num_dict = dict(sorted(BC_dict.items(), reverse=True))
    C = list(C_num_dict.keys())

    key_pointer = 0
    for i in range(N):
        if key_pointer >= len(C):
            break
        a = A[i];r_a = C[key_pointer]
        if a < r_a:
            A[i] = r_a
            C_num_dict[r_a] -= 1
            if C_num_dict[r_a] == 0:
                key_pointer += 1

    print(sum(A))