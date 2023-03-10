#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))

    S_dash = lines[0]
    T = lines[1]

    pointers = []
    for i in range(len(S_dash)-len(T)+1):
        for j in range(len(T)):
            if S_dash[i+j] == T[j] or S_dash[i+j] == '?':
                continue
            else: break
        else:
            pointers.append(i)

    if len(pointers) == 0:
        print('UNRESTORABLE')
        exit()
    else:
        ans_list = []
        for pointer in pointers:
            base_ans = S_dash[:pointer] + T + S_dash[pointer+len(T):]
            ans = base_ans.replace('?','a')
            ans_list.append(ans)
        ans_list = sorted(ans_list)
        print(ans_list[0])
        exit()