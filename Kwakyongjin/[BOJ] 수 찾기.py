import sys
input = sys.stdin.readline

n = int(input())
nl = set(map(int, input().split()))

m = int(input())
ml = list(map(int, input().split()))

for l in ml:
    print(1) if l in nl else print(0)
