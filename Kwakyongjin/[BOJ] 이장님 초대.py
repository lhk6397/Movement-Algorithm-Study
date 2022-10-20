import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = list(map(int, input().split()))
graph.sort(reverse=True)
graph.insert(0,0)

s = []
for idx, val in enumerate(graph):
    s.append(idx + val)    
print(max(s) + 1)
