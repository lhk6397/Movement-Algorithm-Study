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
        if check != lst[i]:
            result.append(lst[i])
            check = lst[i]
            solution(i)
            result.pop()

solution(start)
