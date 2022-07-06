# https://www.acmicpc.net/problem/14425
n, m = map(int, input().split())
cnt = 0
S = dict()
for _ in range(n):
    S[input()] = True
for _ in range(m):
    s = input()
    if s in S.keys(): # 탐색 딕셔너리 사용
        cnt += 1
print(cnt)