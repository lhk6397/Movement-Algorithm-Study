import sys
input = sys.stdin.readline

n = int(input().rstrip())
nlst = list(map(int, input().split()))
nlst = set(nlst)
ans = []

m = int(input().rstrip())
mlst = list(map(int, input().split()))

for num in mlst:
    if num in nlst:
        ans.append(1)
    else:
        ans.append(0)
    
print(*ans)
