# https://www.acmicpc.net/problem/16922
def btr(v, cnt):
    if cnt == n:
        num.add(sum(numbers))
        return
    for i in range(v, 4):
        numbers.append(rome[i])
        btr(i, cnt+1)
        numbers.pop()
rome = [1, 5, 10, 50]
n = int(input())
numbers = []
num = set()

btr(0, 0)
print(len(num))

'''
라이브러리 이용한 풀이
from itertools import combinations_with_replacement
n = int(input())
rome = [1, 5, 10,50]
temp = list(combinations_with_replacement(rome, n))
result = set()
for i in temp:
    result.add(sum(i))
print(len(result))
'''