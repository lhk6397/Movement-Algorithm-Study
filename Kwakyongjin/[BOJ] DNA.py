import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
graph.sort()
result = ""
cnt = 0

for i in range(m):
    s = [['A', 0],['C', 0],['G', 0],['T', 0]]
    for j in range(n):
        for k in range(4):
            if graph[j][i] == s[k][0]:
                s[k][1] += 1
    
    s.sort(key=lambda x:(-x[1], x[0]))
    result += s[0][0]
    cnt += n-s[0][1]

print(result)
print(cnt)
