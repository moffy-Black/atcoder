#!/opt/homebrew/bin/python
import sys

def prime_factorization(N,M):
    X=N**2
    a = 1
    while a <= M**0.5+1:
        b = M/a
        if M%a==0 and b <= N:
            return M
        else:
            b = int(b)+1
            if b <= N:
                X = min(X, a*b)
        a+=1
    return X

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,M = map(int, lines[0].split())
    if N**2 < M:
        print(-1)
        exit()
    print(prime_factorization(N,M))
