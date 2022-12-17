#!/opt/homebrew/bin/python
import sys
import string

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    S = lines[0]
    str_all = list(string.ascii_lowercase)
    if S == "zyxwvutsrqponmlkjihgfedcba":
        ans = -1
    elif len(S) < 26:
        for s in S:
            str_all.remove(s)
        ans = S+str_all[0]
    else:
        candidate = []
        for i in range(25, 0, -1):
            candidate.append(S[i])
            if S[i-1] < S[i]:
                for t in sorted(candidate):
                    if S[i-1] < t:
                        ans = S[:i-1] + t
                        break
                break
    print(ans)

