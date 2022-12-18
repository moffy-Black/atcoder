#!/opt/homebrew/bin/python
import sys
from collections import deque


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n').split())
    N,M = map(int, lines[0])
    uv_list = list(map(tuple,lines[1:]))
    uv_dict = {i:set() for i in range(1,N+1)}
    for uv in uv_list:
        u,v = map(int,(uv))
        uv_dict[u].add(v);uv_dict[v].add(u)

    ans = 0
    for i in range(1,N+1):
        if len(uv_dict[i]) == N-1:
            continue
        que = deque([{i}])
        visited = set()
        cnt = 0
        while True:
            nodes = que[0]
            tmp_que = set()
            for node in nodes:
                visited.add(node)
                neighbor = uv_dict[node]-visited
                if cnt % 2 == 0 and cnt !=0:
                    ans += len(neighbor-uv_dict[i])
                    for k in neighbor-uv_dict[i]:
                        uv_dict[k] |= {i}
                    uv_dict[i] |= neighbor
                tmp_que |= neighbor
            if len(tmp_que) == 0:
                break
            que.append(tmp_que)
            que.popleft()
            cnt += 1
    print(ans)
