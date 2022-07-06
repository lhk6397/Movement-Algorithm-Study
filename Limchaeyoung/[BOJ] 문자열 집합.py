# https://www.acmicpc.net/problem/14425
n, m = map(int, input().split())
cnt = 0
S = []
T = []
for s in range(n):
    S.append(input())
for t in range(m):
    T.append(input())
for x in T:
    if x in S:
        cnt += 1
print(cnt)