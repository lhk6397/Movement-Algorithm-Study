from sys import stdin as stdi
str = stdi.readline()
result = ""
stack = []
check = False
for i in range(len(str)):
  if str[i] == '<' or str[i] == '>' or str[i] == ' ' or i == len(str) - 1:
    if str[i] == '>':
      check = False
      stack.reverse()
    if check:
      stack.append(str[i])
      continue
    else:
      while(stack):
        result += stack.pop()
      result += str[i]
      if str[i] == '<':
        check = True
  else:
    stack.append(str[i])
print(result)
