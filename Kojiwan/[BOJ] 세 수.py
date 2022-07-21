import sys

a, b, c = map(int, sys.stdin.readline().split())

if (a >= b and b >= c) or (c >= b and b >= a):
  print(b)
elif (a >= c and c >= b) or (b >= c and c >= a):
  print(c)
else:
  print(a)