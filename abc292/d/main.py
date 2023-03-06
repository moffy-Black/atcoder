#!/opt/homebrew/bin/python
import sys
from collections import deque

def bfs(start, node_path, arrived_node, cnt_dict, parent_dict):
    que = deque([start])
    while que:
        v = que.popleft()
        if arrived_node[v]: continue
        arrived_node[v] = True;cnt_dict["node_num"] += 1
        for node in node_path[v]:
            if node in parent_dict[v]: continue
            if not arrived_node[node]:
                que.append(node)
                parent_dict[node].add(v)
            cnt_dict["edge_num"] += 1


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,M = map(int, lines[0].split())
    node_path = [[] for _ in range(N)]
    for line in lines[1:]:
        a,b = map(int, line.split())
        if a==b:
            node_path[a-1].append(b-1)
        else:
            node_path[a-1].append(b-1); node_path[b-1].append(a-1)

    arrived_node = [False for _ in range(N)];parent_dict = {i:set() for i in range(N)}
    for i in range(N):
        cnt_dict = {"node_num": 0, "edge_num": 0}
        if arrived_node[i]: continue
        bfs(i, node_path, arrived_node, cnt_dict, parent_dict)
        if cnt_dict["node_num"] != cnt_dict["edge_num"]:
            print("No")
            sys.exit()
    print("Yes")
