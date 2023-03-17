#!/opt/homebrew/bin/python
import sys

def prime_factorization(N):
    i = 2
    ret = {}
    while i * i <= N:
        while N % i == 0:
            N //= i
            if i in ret:
                ret[i] += 1
            else:
                ret[i] = 1
        i += 1
    if N != 1:
        ret[N] = 1
    return ret

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    a, b = map(int, lines[0].split())
    a_prime = prime_factorization(a);b_prime = prime_factorization(b)
    a_prime_set = set(a_prime.keys());b_prime_set = set(b_prime.keys())
    print(len(a_prime_set & b_prime_set)+1)
