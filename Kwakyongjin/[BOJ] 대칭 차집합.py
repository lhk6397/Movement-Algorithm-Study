import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = set(map(int, input().split()))
cnt = 0

for i in range(n):
    if a[i] in b:
        cnt += 1

print(n+k-2*cnt)
