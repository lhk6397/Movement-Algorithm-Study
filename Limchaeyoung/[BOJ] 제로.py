# https://www.acmicpc.net/problem/10773
data = []
k = int(input())
for x in range(k):
    n = int(input())
    data.pop() if n == 0 else data.append(n)
print(sum(data))