#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,K = map(int,lines[0].split())
    user_list = lines[1:]
    sorted_list = sorted(user_list[:K])
    for i in range(K):
        print(sorted_list[i])