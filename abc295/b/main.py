#!/opt/homebrew/bin/python
import sys
import copy

def manhattan_coords(x, origin=(0,0)):
    """
    Return a list of coordinates that have a Manhattan distance of x from a given origin.

    Args:
        x (int): the Manhattan distance to search for
        origin (tuple): the starting coordinates, defaults to (0,0)

    Returns:
        list: a list of tuples representing coordinates with Manhattan distance x from the origin
    """
    coords = []
    for i in range(-x, x+1):
        for j in range(-x, x+1):
            if abs(i) + abs(j) <= x:
                coords.append((origin[0] + i, origin[1] + j))
    return coords

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    R,C = map(int, lines[0].split())
    masu_map = []
    for i in range(1, R+1):
        masu_map.append(list(lines[i]))

    ans_masu_map = copy.deepcopy(masu_map)
    for i in range(R):
        for j in range(C):
            masu = masu_map[i][j]
            if masu == "." or masu == "#":
                continue
            else:
                masu = int(masu)
                candidates = manhattan_coords(masu, (i,j))
                for y,x in candidates:
                    if 0 <= y and y < R and 0 <= x and x < C:
                        if not masu_map[y][x] == ".":
                            ans_masu_map[y][x] = "."

    for i in range(R):
        print("".join(ans_masu_map[i]))
