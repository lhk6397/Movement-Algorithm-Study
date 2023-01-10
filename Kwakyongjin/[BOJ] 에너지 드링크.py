import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = list(map(int, input().split()))
graph.sort()

ans = graph.pop()
for i in range(n-1):
    ans += graph[i]/2

print(ans)
