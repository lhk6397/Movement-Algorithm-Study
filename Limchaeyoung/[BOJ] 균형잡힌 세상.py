# https://www.acmicpc.net/problem/4949
while True:
    stack = []
    s = input()
    if s == '.':
        break
    for x in range(len(s)):
        if s[x] == '(' or s[x]:
            stack.append(s[x])
        elif s[x] == ')':
            if not stack:
                stack.append(0)
                break
            if stack.pop() != '(':
                stack.append(0)
                break
        elif s[x] == ']':
            if not stack:
                stack.append(0)
                break
            if stack.pop() != '[':
                stack.append(0)
                break
    if not stack:
        print("yes")
    else:
        print("no")