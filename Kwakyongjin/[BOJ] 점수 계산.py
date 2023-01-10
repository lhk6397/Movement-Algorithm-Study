import sys
input = sys.stdin.readline

graph = {}
for i in range(8):
    num = int(input().rstrip())
    graph[num] = i+1

graph = sorted(graph.items(), key = lambda x:-x[0])

score = 0
result = []
for i in range(5):
    score += graph[i][0]
    result.append(graph[i][1])

print(score)
result.sort()
print(*result)
