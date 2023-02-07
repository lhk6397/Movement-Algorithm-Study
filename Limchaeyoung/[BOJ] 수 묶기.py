# https://www.acmicpc.net/problem/1744
n = int(input())
data = [int(input()) for i in range(n)]
data.sort(reverse=True)
idx, sum, num = len(data), 0, 0

for i, d in enumerate(data):
    if d < 1:
        idx = i
        break

data1, data2 = data[:idx], data[idx:]
data2.reverse()

if data1:
    for i, d in enumerate(data1):
        if d == 1:
            sum += 1
            continue
        if i % 2 == 0:
            num = d
        else:
            num *= d
            sum += num
            num = 0
    if num != 0: sum += num
if data2:
    for i, d in enumerate(data2):
        if i % 2 == 0:
            num = d
        else:
            num *= d
            sum += num
            num = 0
    if num != 0: sum += num

print(sum)

