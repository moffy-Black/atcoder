#!/opt/homebrew/bin/python
import sys
import string


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    K = int(lines[0])
    print(string.ascii_uppercase[:K])