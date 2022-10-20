import sys
input = sys.stdin.readline

n = int(input().rstrip())
person = [list(map(int, input().split())) for _ in range(n)]
answer = [0] * n

for i in range(n):
    k = 1
    for j in range(n):
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            k += 1
    
    answer[i] = k

print(*answer)
