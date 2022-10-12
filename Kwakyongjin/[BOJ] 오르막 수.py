d = [1] * 11
d[0] = 0

n = int(input())
for _ in range(n-1):
    for i in range(1, 11):
        d[i] += d[i-1]

print(sum(d)%10007)
