import sys
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())
location = list(map(int, input().split()))
total = 0

if n <= k:
    print(total)

else:
    location.sort()
    dist = []
    for i in range(1, n):
        dist.append(location[i] - location[i - 1])

    dist.sort(reverse=True)

    for _ in range(k-1):
        dist.pop(0)
        
    print(sum(dist))
