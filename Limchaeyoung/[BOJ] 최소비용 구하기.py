import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
d = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # (노드, 비용)

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start)) # (비용, 노드)
    d[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if now == end:
            return dist
        if d[now] < dist:
            continue
        for g in graph[now]:
            cost = dist + g[1]
            if d[g[0]] > cost:
                d[g[0]] = cost
                heapq.heappush(q, (cost, g[0]))

start, end = map(int, input().split())
print(dijkstra(start, end))