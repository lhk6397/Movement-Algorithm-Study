# https://www.acmicpc.net/problem/10814
user = []
n = int(input())
for _ in range(n):
    user.append(list(input().split()))
user = sorted(user, key=lambda x: int(x[0]))
for y in range(n):
    print(user[y][0], user[y][1])