import sys
input = sys.stdin.readline

graph = list(input().rstrip())
stack = []
ans = 0

for i in range(len(graph)):
    if graph[i] == '(':
        stack.append(graph[i])
    
    else:
        if graph[i-1] == '(':
            stack.pop()
            ans += len(stack)
        
        else:
            stack.pop()
            ans += 1

print(ans)
