import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().split()))
a.sort()
print(*a)
