import sys
input = sys.stdin.readline

S = input().rstrip()
lst = []
for i in range(len(S)):
    lst.append(S[i:])

lst = sorted(lst)
print(*lst, sep='\n')
