import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

lst = sorted(lst)
print(*lst, sep='\n')
