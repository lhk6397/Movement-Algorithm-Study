def solution(a, b):
    if b == 1:
        return a % C
    
    mod = solution(a, b // 2)

    if b % 2 == 0:
        return mod * mod % C
    
    if b % 2 == 1:
        return mod * mod * a % C

A, B, C = map(int, input().split())
print(solution(A, B))
