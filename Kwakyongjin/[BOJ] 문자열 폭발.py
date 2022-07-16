mes = input()
bomb = list(input())
answer = []
n = len(bomb)

for i in mes:
    answer.append(i)
    if i == bomb[-1]:
        if bomb == answer[-n:]:
            for j in range(n):
                answer.pop()


if answer:
    print(''.join(answer))
else:
    print('FRULA')
