#!/opt/homebrew/bin/python
import sys
sys.setrecursionlimit(10**9)

def recr(node_list, node, parent, tmp_value, value_dict, ans):
    if node in value_dict:
        tmp_value += value_dict[node]
    ans[node] += tmp_value
    for i in node_list[node]:
        if i == parent:
            continue
        recr(node_list, i, node, tmp_value, value_dict, ans)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))

    N,M = map(int, lines[0].split());ans = [0 for _ in range(N)]

    node_list = [[] for _ in range(N)]
    for i in range(1,N):
        a,b = map(int, lines[i].split())
        node_list[a-1].append(b-1);node_list[b-1].append(a-1)

    value_dict = dict()
    for i in range(N,N+M):
        n,v = map(int, lines[i].split())
        value_dict.setdefault(n-1,0)
        value_dict[n-1] += v

    _ = recr(node_list, 0, -1, 0, value_dict, ans)

    print(" ".join(map(str, ans)))

