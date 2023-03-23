#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    location = list(map(int, lines[0].split(' ')))
    if location[0] != 0:
        location[2] -= location[0];location[0] -= location[0]
    if location[1] != 0:
        location[3] -= location[1];location[1] -= location[1]
    ans = ""
    for i in range(location[3]):
        ans += "U"
    for i in range(location[2]):
        ans += "R"
    for i in range(location[3]):
        ans += "D"
    for i in range(location[2]):
        ans += "L"
    ans += "L"
    for i in range(location[3] + 1):
        ans += "U"
    for i in range(location[2] + 1):
        ans += "R"
    ans += "DR"
    for i in range(location[3] + 1):
        ans += "D"
    for i in range(location[2] + 1):
        ans += "L"
    ans += "U"
    print(ans)
