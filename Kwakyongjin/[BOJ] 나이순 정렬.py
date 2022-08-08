import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    a, b = input().split()
    a = int(a)
    lst.append((a, b))

lst = sorted(lst, key=lambda x : x[0])
for i in range(n):
    print(lst[i][0], lst[i][1])
