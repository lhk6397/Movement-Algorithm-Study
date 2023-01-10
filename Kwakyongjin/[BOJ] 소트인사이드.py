import sys
input = sys.stdin.readline

s = list(input().rstrip())
s.sort(reverse=True)
print(*s, sep='')
