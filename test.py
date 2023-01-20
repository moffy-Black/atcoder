#!/opt/homebrew/bin/python
import sys

def parse_data(lines):
  N = int(lines[0])
  a_list = list(map(int,lines[1].split()))
  b_list = list(map(int,lines[2].split()))
  return N,a_list,b_list

def extract_distance(a_list,b_list):
  return [a-b for a,b in zip(a_list,b_list)]

def judge_enable_compose(distance_list):
  return False if sum(distance_list)>=0 else True

def extract_min_prepare_num(N,distance_list):
  sorted_dis_list = sorted(distance_list)
  num_cnt,debt=0,0
  for i in range(N):
    if sorted_dis_list[i] >= 0:
      break
    debt += sorted_dis_list[i]
    num_cnt+=1
  if debt != 0:
    for i in range(N-1,-1,-1):
      debt += sorted_dis_list[i]
      num_cnt+=1
      if debt >= 0:
        break
  return num_cnt

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    N,a_list,b_list = parse_data(lines)
    distance_list = extract_distance(a_list,b_list)
    if judge_enable_compose(distance_list):
      print(-1)
    else:
      ans = extract_min_prepare_num(N,distance_list)
      print(ans)