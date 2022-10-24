import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = list(map(int, input().split()))
graph.sort()
print(graph[k-1])
