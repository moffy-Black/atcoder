#!/opt/homebrew/bin/python
import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N = int(lines[0])
    a_list = list(map(int, lines[1].split()))

    a_dict = dict()
    for a in a_list:
        a_dict.setdefault(a,0)
        a_dict[a]+=1

    if len(a_dict) == 1 and list(a_dict.keys())[0] == 0:
        print("Yes")
    elif len(a_dict) == 2:
        if list(a_dict.values())[0] < list(a_dict.values())[1]:
            if list(a_dict.keys())[0] == 0 and list(a_dict.values())[0]*2==list(a_dict.values())[1]:
                print("Yes")
            else:
                print("No")
        else:
            if list(a_dict.keys())[1] == 0 and list(a_dict.values())[1]*2==list(a_dict.values())[0]:
                print("Yes")
            else:
                print("No")
    elif len(a_dict) == 3 and (list(a_dict.keys())[0]^list(a_dict.keys())[1]^list(a_dict.keys())[2]==0) and (list(a_dict.values())[0]==list(a_dict.values())[1] and list(a_dict.values())[0]==list(a_dict.values())[2]):
        print("Yes")
    else:
        print("No")