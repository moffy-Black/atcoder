#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,M = map(int, lines[0].split())
    estimation = {0}
    box_ball_num = [1 for _ in range(N)]
    for line in lines[1:]:
        x,y = map(int, line.split())
        box_ball_num[x-1]-=1;box_ball_num[y-1]+=1
        if x-1 in estimation:
            if box_ball_num[x-1] == 0:
                estimation.remove(x-1)
            estimation.add(y-1)
    print(len(estimation))