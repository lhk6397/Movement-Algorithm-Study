# https://www.acmicpc.net/problem/9935
S = list(input())
bomb = list(input())
stack = []
for s in S:
    stack.append(s)
    if len(stack) >= len(bomb):
        if stack[-len(bomb):] == bomb:
            for _ in range(len(bomb)):
                stack.pop()
'''
for s in S:
    if s == bomb[len(bomb)-1]:
        if len(stack) >= len(bomb)-1:
            stack2 = [s]
            for i in range(len(bomb)-1, 0, -1):
                k = stack.pop()
                if k == bomb[i-1]:
                    stack2.append(k)
                else:
                    stack.append(k)
                    while stack2:
                        stack.append(stack2.pop())
                    break
        else:
            stack.append(s)
    else:
        stack.append(s)
'''
if stack:
    print(''.join(stack))
else:
    print('FRULA')