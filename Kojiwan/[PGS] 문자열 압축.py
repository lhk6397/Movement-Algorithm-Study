# https://programmers.co.kr/learn/courses/30/lessons/60057

def conditional_print(count, s_comp, last_unit):
  if count > 1:
    temp = str(count) + last_unit
    s_comp += temp
  else:
    s_comp += last_unit
  return s_comp

def solution(s):
  min_length = len(s)
  for unit in range(1, len(s) // 2 + 1, 1):
    s_comp = ""
    count = 1
    last_unit = s[0: unit]
    for st in range(unit, len(s) + 1, unit):
      ed = st + unit
      if ed > len(s):
        s_comp = conditional_print(count, s_comp, last_unit)
        s_comp += s[st:]
        break
      if last_unit == s[st:ed]:
        count += 1
      else:
        s_comp = conditional_print(count, s_comp, last_unit)
        count = 1
      last_unit = s[st:ed]
    if(min_length > len(s_comp)):
      min_length = len(s_comp)
  return min_length

print(solution(	"ababcdcdababcdcd"))