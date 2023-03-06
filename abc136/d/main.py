#!/opt/homebrew/bin/python
import sys
import math

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    S = lines[0];ans=[0 for _ in range(len(S))]
    return_flag=False;return_point=0;cnt_dict={"R":0,"L":0}
    i=0
    for s in S:
        if not return_flag:
            if s == "L":
                cnt_dict["L"] += 1
                return_point=i-1;return_flag = True
            else:
                cnt_dict["R"] += 1
        else:
            if s =="L":
                cnt_dict["L"] += 1
            else:
                ans[return_point] = math.ceil(cnt_dict["R"]/2) + cnt_dict["L"]//2
                ans[return_point+1] = math.ceil(cnt_dict["L"]/2) + cnt_dict["R"]//2
                return_flag=False;cnt_dict={"R":1,"L":0}
        i += 1
    else:
        if return_flag:
            ans[return_point] = math.ceil(cnt_dict["R"]/2) + cnt_dict["L"]//2
            ans[return_point+1] = math.ceil(cnt_dict["L"]/2) + cnt_dict["R"]//2
    print(" ".join(list(map(str,ans))))
