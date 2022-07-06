n = int(input())
answers = []
stack = []
num = 0
theta = True

for i in range(n):
    data = int(input())

    while num < data: # 예) data = 5일 때 stack = [1,2,3,4,5] 까지
        num += 1
        stack.append(num)
        answers.append('+')
        
    if data == stack[-1]:
        stack.pop()
        answers.append('-')
        
    else:
        theta = False
        break

if theta == False:
    print('NO')
else:
    print('\n'.join(answers))
