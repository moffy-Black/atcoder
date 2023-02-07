#!/opt/homebrew/bin/python
import sys
import collections

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,P = map(int,lines[0].split())
    c = collections.Counter(prime_factorize(P))
    ans = 1
    for k,v in c.items():
        ans*=k**(v // N)
    print(ans)

