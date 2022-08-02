from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

com = [i for i in range(1, n+1)]
result = list(combinations(com, m))
for i in result:
    i = list(i)
    print(*i)

