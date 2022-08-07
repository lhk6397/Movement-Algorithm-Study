import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)
result = []
visited = [False] * n

def solution():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    check = 0
    for i in range(n):
        if not visited[i] and check != lst[i]:
            result.append(lst[i])
            visited[i] = True
            check = lst[i]
            solution()
            result.pop()
            visited[i] = False
         
solution()
    
