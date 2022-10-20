import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = list(map(int, input().split()))
graph.sort()
result = []
for i in range(n):
    result.append(graph[i] + graph[(2*n-1)-i])

print(min(result))
