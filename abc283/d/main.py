#!/opt/homebrew/bin/python
import sys
from collections import deque

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    S = lines[0]
    pointer_list = []
    boll_list = []
    boll_pointer = -1
    box = set()

    for i in range(len(S)):
        if S[i] == "(":
            pointer_list.append(i)
            boll_list.append(set())
            boll_pointer += 1
        elif S[i] == ")":
            delete_ball = boll_list[boll_pointer]
            box -= delete_ball
            pointer_list.pop()
            boll_pointer -= 1
        else:
            if S[i] in box:
                print("No")
                break
            else:
                if boll_pointer != -1:
                    boll_list[boll_pointer].add(S[i])
                box.add(S[i])
    else:
        print("Yes")
