#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    a_list = list(map(int,lines[1].split()))
    Q = int(lines[2])
    queries = lines[3:]

    for i in range(Q):
        query = list(map(int,queries[i].split()))
        if query[0] == 1:
            a_list[query[1]-1] = query[2]
        else:
            print(a_list[query[1]-1])