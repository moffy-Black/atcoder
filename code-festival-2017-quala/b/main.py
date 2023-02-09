#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,M,K = map(int, lines[0].split())
    for i in range(N+1):
        for j in range(M+1):
            tmp_ans = (M*i) + (N*j) - 2*(i*j)
            if K==tmp_ans:
                print("Yes")
                exit(0)
    else:
        print("No")