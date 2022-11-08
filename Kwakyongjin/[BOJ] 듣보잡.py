import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nlst = [input().rstrip() for _ in range(n)]
nlst = set(nlst)
ans = []

for i in range(m):
    s = input().rstrip()

    if s in nlst:
        ans.append(s)

ans.sort()
print(len(ans))
print(*ans, sep='\n')
