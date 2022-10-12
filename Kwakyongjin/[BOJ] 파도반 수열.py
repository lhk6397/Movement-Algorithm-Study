import sys
input = sys.stdin.readline

p = [0] * 101
p[1] = 1
p[2] = 1
p[3] = 1
for i in range(4, 101):
    p[i] = p[i-2] + p[i-3]

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    print(p[n])
