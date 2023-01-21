#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    S = lines[1]
    cnt = 0;pointer=[]
    for i in range(N-1):
        if S[i]=="n" and S[i+1]=="a":
            pointer.append(i+1+cnt)
            cnt += 1
    for j in pointer:
        S = S[:j] + "y" + S[j:]
    print(S)