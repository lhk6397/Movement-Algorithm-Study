# https://www.acmicpc.net/status?user_id=hea_c&problem_id=11047&from_mine=1
n, k = map(int, input().split())
value = []
cnt = 0
for _ in range(n):
    value.append(int(input()))
for x in range(n-1, -1, -1):
    if k < value[x]:
        continue
    cnt += k // value[x]
    k %= value[x]
    if k == 0:
        break
print(cnt)