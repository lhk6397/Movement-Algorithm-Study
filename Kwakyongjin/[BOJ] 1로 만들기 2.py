import sys
input = sys.stdin.readline

n = int(input().rstrip())
d = [[0,[]] for _ in range(n+1)]
d[1] = 0
table = [[] for _ in range(n+1)]
table[1] = [1]


for i in range(2, n+1):
    d[i] = d[i-1] + 1
    table[i] = table[i-1] + [i]
    if i % 3 == 0 and d[i//3] + 1 < d[i]:
        d[i] = d[i//3] + 1
        table[i] = table[i//3] + [i]

    if i % 2 == 0 and d[i//2] + 1 < d[i]:
        d[i] = d[i//2] + 1
        table[i] = table[i//2] + [i]

print(d[n])
print(*reversed(table[n]))
