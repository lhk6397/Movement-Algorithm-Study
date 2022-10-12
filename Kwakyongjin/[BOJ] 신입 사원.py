import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    rank = [[int(i) for i in input().split()] for _ in range(n)]
    cnt = 0
    rank.sort()

    high_rank = rank[0][1]
    cnt += 1

    for i in range(n):
        if rank[i][1] < high_rank:
            high_rank = rank[i][1]
            cnt += 1

    print(cnt)
