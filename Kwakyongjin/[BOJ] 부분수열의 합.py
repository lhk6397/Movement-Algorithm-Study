import sys
input = sys.stdin.readline
    
def solution(start):
    global count
    if sum(result) == s and len(result) != 0:
        count += 1

    for i in range(start, n):
        result.append(lst[i])
        solution(i+1)
        result.pop()
    
n, s = map(int, input().split())
lst = list(map(int,input().split()))
start = 0
count = 0
result = []
solution(start)
print(count)
