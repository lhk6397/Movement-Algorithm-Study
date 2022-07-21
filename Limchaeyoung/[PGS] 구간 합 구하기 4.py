import sys
input = sys.stdin.readline
N,M = map(int, input().split())
data = list(map(int, input().split()))
pre_sum = [0]

sum = 0
for x in data:
    sum += x
    pre_sum.append(sum)

for y in range(M):
    a, b = map(int, input().split())
    print(pre_sum[b]-pre_sum[a-1])
