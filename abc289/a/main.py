#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    s = lines[0]
    ans = ""
    for i in s:
        if i=="0":
            ans+="1"
        else:
            ans+="0"
    print(ans)