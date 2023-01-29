#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,M = map(int,lines[0].split())
    if M == 0:
        print("No")
    else:
        path_dict = {i+1:set() for i in range(N)}
        for line in lines[1:]:
            u,v = map(int,line.split())
            path_dict[u].add(v);path_dict[v].add(u)
        cnt = 0
        tmp = []
        for k,v in list(path_dict.items()):
            if len(v) == 1:
                cnt += 1
                tmp.append(k)
            elif len(v) == 2:
                continue
            else:
                print("No")
                break
        else:
            if cnt == 2:
                s=tmp[0];e=tmp[1]
                arrived={s};arrived_num = len(arrived)
                node=s
                while True:
                    next = path_dict[node]
                    sa = next-arrived
                    arrived |= next;arrived_num+=1
                    if len(arrived) == arrived_num:
                        node = list(sa)[0]
                        continue
                    else:
                        break
                if len(arrived)==N:
                    print("Yes")
                else:
                    print("No")

            else:
                print("No")