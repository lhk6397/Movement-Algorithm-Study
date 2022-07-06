n = int(input())
q = list(input())
dic = {}
for i in range(1, n+1):
    dic[chr(64+i)] = int(input()) # 딕셔너리, 아스키코드 이용해서 저장 
stack = []
for i in q:
    if i in dic:
        stack.append(dic[i])
    else:
        b, a = stack.pop(), stack.pop()

        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(a - b)
        elif i == '/':
            stack.append(a / b)
        elif i == '*':
            stack.append(a * b)

print("{:.2f}".format(sum(stack)))
