import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = set()

for i in range(n):
    tmp = input().split()

    if tmp[1] == 'enter':
        graph.add(tmp[0])
    else:
        graph.remove(tmp[0])

graph = sorted(list(graph), reverse=True)
print(*graph, sep='\n')
