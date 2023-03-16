#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,M = map(int,lines[0].split())
    A = [];B = []
    for line in lines[1:N+1]:
        A.append(line)
    for line in lines[N+1:]:
        B.append(line)
    for h in range(N-M+1):
        for w in range(N-M+1):
            pointer = h,w
            for i in range(M):
                if A[h+i][w:w+M] != B[i]:
                    break
            else:
                print('Yes')
                sys.exit()
    else:
        print('No')
        sys.exit()