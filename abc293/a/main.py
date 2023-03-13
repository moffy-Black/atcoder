#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    S = list(lines[0])
    for i in range(len(S)-1):
        if i >= len(S) // 2:
            break
        S[2*i], S[2*i+1] = S[2*i+1], S[2*i]
    print(''.join(S))
