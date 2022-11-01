import sys
from collections import deque
import copy
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, tmp = map(int, input().split())
    if n == 1:
        graph = int(input())
        print(1)
    
    else:
        graph = list(map(int, input().split()))
        graph_index = [i for i in range(n)]
        graph_max = copy.deepcopy(graph)
        graph_max.sort(reverse=True)
        graph = deque(graph)
        graph_max = deque(graph_max)
        graph_index = deque(graph_index)
        cnt = 0

        while tmp in graph_index:
            if graph[0] == graph_max[0]:
                graph.popleft()
                graph_max.popleft()
                graph_index.popleft()
                cnt += 1
            else:
                graph.append(graph.popleft())
                graph_index.append(graph_index.popleft())
        print(cnt)  
