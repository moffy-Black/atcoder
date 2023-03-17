#!/opt/homebrew/bin/python
import sys

def check_part_arr(S, i, j, k):
    search = [i, j, k];key=0
    for i in range(len(S)):
        if S[i] == search[key]:
            key+=1
            if key == 3:
                return True
    return False

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    S_str = lines[1];S_list=[];ans=0
    for i in range(N):
        S_list.append(int(S_str[i]))
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if check_part_arr(S_list, i, j, k):
                    ans+=1
    print(ans)
