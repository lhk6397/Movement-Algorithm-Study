import sys
import itertools
input = sys.stdin.readline

n = int(input())
k = int(input())
graph = [input().rstrip() for _ in range(n)]

result = set()
nPr = itertools.permutations(graph, k)

for tmp in nPr:
    result.add(''.join(list(tmp)))
    
print(len(result))
