import sys
n = int(input())
for i in range(n):
    VPS = list(input())
    answer = []
    result = ''
    while VPS:
        data = VPS.pop()
        if data == '(':
            if answer and answer[-1] == ')':
                answer.pop()
            else:
                result += 'NO'
                break
        else:
            answer.append(data)

    if result == 'NO' or answer:
        print('NO')
    else:
        print('YES')
