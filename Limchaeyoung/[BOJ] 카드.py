from collections import Counter
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
cnt = Counter(data)
print((sorted(cnt, key=lambda x: (cnt[x], -x), reverse=True))[0])