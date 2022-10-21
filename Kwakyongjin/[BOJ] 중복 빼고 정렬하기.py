import sys
input = sys.stdin.readline

n = int(input())
print(*sorted(list(set(list(map(int, input().split()))))))
