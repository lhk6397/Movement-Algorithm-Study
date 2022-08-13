import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)
result = []
visited = [False] * n
start = 0

def solution(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    check = 0
    for i in range(start, n):
        if not visited[i] and check != lst[i]:
            result.append(lst[i])
            visited[i] = True
            check = lst[i]
            solution(i+1)
            result.pop()
            visited[i] = False
         
solution(start)
