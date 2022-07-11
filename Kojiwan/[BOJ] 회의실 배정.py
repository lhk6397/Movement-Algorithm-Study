import readline
from sys import stdin
n = int(stdin.readline())
data = []

for _ in range(n):
  data.append(tuple(map(int, stdin.readline().split())))
  
data.sort(key = lambda x : (x[1], x[0]))

end_time = 0
answer = 0
for st, ed in data:
  if st >= end_time:
    end_time = ed
    answer += 1

print(answer)