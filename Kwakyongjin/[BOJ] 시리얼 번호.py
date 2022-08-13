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
    lst.append(input().rstrip())

lst = sorted(lst, key=lambda x:(len(x), solution(x), x))

print(*lst, sep='\n')
