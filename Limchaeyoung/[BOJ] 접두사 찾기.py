# https://www.acmicpc.net/problem/14426
n, m = map(int, input().split())
S = []
W = []
cnt = 0
for _ in range(n):
    S.append(input())
for _ in range(m):
    W.append(input())

for w in W:
    for s in S:
        if w[0] == s[0]:
            if w == s[:len(w)]:
                cnt += 1
                break
print(cnt)
