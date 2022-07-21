import sys

def check(str, st, ed):
  while st < ed:
    if str[st] == str[ed]:
      st += 1
      ed -= 1
    else:
      return False
  return True

T = int(input())

for _ in range(T):
  str = list(sys.stdin.readline().strip())
  st = 0
  ed = len(str) - 1
  answer = 0
  if str == list(reversed(str)):
    print(0)
  else:
    while(st < ed):
      if str[st] == str[ed]:
        st += 1
        ed -= 1
      else:
        if check(str, st + 1, ed) or check(str, st, ed - 1):
          answer = 1
          break
        else:
          answer = 2
          break
    print(answer)