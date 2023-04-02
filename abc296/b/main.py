#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    grid = [list(l) for l in lines]

    for i in range(8):
        for j in range(8):
            if grid[i][j] == "*":
                x=j;y=i
                break
    col_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
    row_list = [i+1 for i in range(8)]
    print(f"{col_list[x]}{row_list[7-y]}")