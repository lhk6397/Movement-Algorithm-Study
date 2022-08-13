import sys
input = sys.stdin.readline

def solution(a):
    answer = 0
    for i in a:
        if i.isdigit():
            answer += int(i)
    return answer

n = int(input())
lst = []
for i in range(n):
    name, language, english, math = input().split()
    lst.append([name, int(language), int(english), int(math)])

lst = sorted(lst, key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in lst:
    print(i[0])
