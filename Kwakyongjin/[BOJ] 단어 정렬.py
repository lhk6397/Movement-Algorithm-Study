import sys
input = sys.stdin.readline

n = int(input().rstrip())
lst = []
for i in range(n):
    lst.append(input().rstrip())

lst = set(lst)
lst = list(lst)
lst = sorted(lst, key=lambda x:(len(x), x))
print(*lst, sep='\n')
