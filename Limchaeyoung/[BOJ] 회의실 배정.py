# https://www.acmicpc.net/submit/1931/45793630
n = int(input())
time = []
cnt = 1
for x in range(n):
    start, end = map(int, input().split())
    time.append([start, end])
time = sorted(time, key=lambda x: (x[1], x[0])) # - 붙이면 내림차순 정렬
end = time[0][1]
for x in range(1, len(time)):
    if end <= time[x][0]:
        end = time[x][1]
        cnt += 1
print(cnt)