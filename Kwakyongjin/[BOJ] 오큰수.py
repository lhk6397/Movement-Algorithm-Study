# stack에 인덱스를 넣어보는 생각도 좋은 것 같다.
import sys
n = int(input())
lst = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and lst[stack[-1]] < lst[i]:
        answer[stack.pop()] = lst[i]
    stack.append(i)

print(*answer) # list를 출력하는 방법
