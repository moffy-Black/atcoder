#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,M = map(int, lines[0].split())
    A = list(map(int, lines[1].split()))
    B = list(map(int, lines[2].split()))
    C_list = sorted(A + B)

    A_dict = {a:0 for a in A};B_dict = {b:0 for b in B}
    for i in range(N+M):
        c = C_list[i]
        if c in A_dict:
            A_dict[c] = i+1
        else:
            B_dict[c] = i+1

    print(" ".join(map(str, list(A_dict.values()))))
    print(" ".join(map(str, list(B_dict.values()))))