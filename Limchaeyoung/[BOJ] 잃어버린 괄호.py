# https://www.acmicpc.net/problem/1541
st = input().split('-')
num = []
for s in st:
    n = 0
    ii = s.split('+')
    for i in ii:
        n += int(i)
    num.append(n)
answer = num[0] * 2 - sum(num)
print(answer)