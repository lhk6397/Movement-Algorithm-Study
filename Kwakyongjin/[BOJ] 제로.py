k = int(input())
stack = []
for _ in range(k):
    data = int(input())
    if data == 0:
        stack.pop()
    else:
        stack.append(data)
print(sum(stack))
