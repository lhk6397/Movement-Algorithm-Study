import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = {}
for i in range(1, n+1):
    s = input().rstrip()
    graph[i] = s

graph2 = {v:k for k,v in graph.items()}

for i in range(m):
    s = input().rstrip()

    if s.isdigit():
        print(graph[int(s)])
    
    else:
        print(graph2[s])
