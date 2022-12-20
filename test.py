#!/opt/homebrew/bin/python
import csv


class InputCSVError(Exception):
  pass

class LargeDataError(Exception):
  pass

class RowsCSVError(Exception):
  pass

class UsrCSVError(Exception):
  pass

def csv_input(csv_path) -> tuple[list,Exception]:
  try:
    with open(csv_path, encoding='Shift_JIS') as f:
      reader = csv.reader(f)
      return [row for row in reader],None
  except Exception as e:
    return [],e

def score_cnt(reader) -> tuple[dict,list]:
  usr_score_cnt = dict();err_row=[]
  for read in reader:
    try:
      usr=read[1];score=int(read[2])
    except Exception:
      err_row.append(read[0])
    usr_score_cnt.setdefault(usr,[0]*3)
    usr_score_cnt[usr][0]+=1;usr_score_cnt[usr][1]+=int(score)
  return usr_score_cnt,err_row

def calc_mean(usr_score_cnt) -> list:
  usr_mean_score=dict();err_usr = []
  for k in usr_score_cnt.keys():
    try:
      usr_mean_score.setdefault(k,round(usr_score_cnt[k][1] / usr_score_cnt[k][0]))
    except Exception:
      err_usr.append(k)
  return usr_mean_score, err_usr

if __name__ == '__main__':
  csv_path = './sample.csv'
  csv_reader,err = csv_input(csv_path)
  if err != None:
    raise InputCSVError(err)
  elif len(csv_reader) > 10**6:
    raise LargeDataError('csvファイルのrowが10の6乗より多いです')

  usr_score_cnt,err_row = score_cnt(csv_reader)
  if len(err_row) > 0:
    raise RowsCSVError(f'csvファイルに問題のある行があります\n{err_row}')

  usr_mean_score,err_usr = calc_mean(usr_score_cnt)
  if len(err_usr) > 0:
    raise UsrCSVError(f'scoreの平均が計測できなかったユーザがいます\n{err_usr}')

  sorted_usr_mean_score = dict( sorted(usr_mean_score.items(), key=lambda x:x[1],reverse=True))

  cnt = 0;tmp_value=0
  for k,v in sorted_usr_mean_score.items():
    if tmp_value == v:
      print(f'{k},{v}');tmp_value=v
    elif cnt < 10:
      print(f'{k},{v}');cnt+=1