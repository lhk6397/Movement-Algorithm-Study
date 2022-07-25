# https://www.acmicpc.net/submit/1654/46575033
def binary_search(start, end, target):
    while start <= end:
        cnt = 0
        global max
        mid = (start + end) // 2
        for l in line:
            cnt += l // mid
        if cnt >= target:
            if max < mid:
               max = mid
            start = mid + 1
        else:
            end = mid - 1
max = 0
k, n = map(int, input().split())
line = []
for _ in range(k):
    line.append(int(input()))
binary_search(1, sum(line)//n, n)
print(max)