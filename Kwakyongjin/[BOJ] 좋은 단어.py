import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0
for _ in range(n):
    word = list(input().rstrip())
    stack = []

    for i in range(len(word)):
        if stack:
            if stack[-1] == word[i]:
                stack.pop()
            
            else:
                stack.append(word[i])
        
        else:
            stack.append(word[i])
    
    if not stack:
        cnt += 1
    
print(cnt)
