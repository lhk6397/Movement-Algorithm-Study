import sys

s = sys.stdin.readline().rstrip()
stack = []
answer = 0 

for i in s:
    if i == '(' or i == '[':
        stack.append(i)
    
    if i == ')':
        if not stack:
            print(0)
            exit(0)
        theta = 0
        while len(stack) != 0:
            temp = stack.pop()
        
            if temp == '(':
                if theta == 0:
                    stack.append(2)
                else:
                    stack.append(2*theta)
                break

            elif temp == '[':
                print(0)
                exit(0)
            else:
                theta += temp
            
    if i == ']':
        if not stack:
            print(0)
            exit(0)
        theta = 0
        while len(stack) != 0:
            temp = stack.pop()
            
            if temp == '[':
                if theta == 0:
                    stack.append(3)
                else:
                    stack.append(3*theta)
                break
            
            elif temp == '(':
                print(0)
                exit(0)
            else:
                theta += temp

for i in stack:
    if i == '(' or i == '[':
        print(0)
        exit(0)
    else:
        answer += i

print(answer)
