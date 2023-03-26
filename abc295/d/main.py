#!/opt/homebrew/bin/python
import sys
import math

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    S = lines[0]
    previous = 0;previous_dict = {0:1}

    for i in range(len(S)):
        s = int(S[i])
        previous ^= (1 << s)
        previous_dict.setdefault(previous, 0)
        previous_dict[previous] += 1

    previous_duplicated = list(previous_dict.values());ans = 0
    for i in range(len(previous_duplicated)):
        ans += math.comb(previous_duplicated[i], 2)

    print(ans)