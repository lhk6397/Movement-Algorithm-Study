# 재귀로 해결하려고 했다가 오류남
import sys

def solution(x, y, n):
    global answer, r, c
    temp = (2**(n-1))**2
    all = n ** 2
    if r == x and r == y:
        return print(answer)

    if n == 1:
        if r - x == 0 and c - y == 1:
            return print(answer + 1)
        if r - x == 1 and c - y == 0:
            return print(answer + 2)
        if r - x == 1 and c - y == 1:
            return print(answer + 3)

    if y + all // 2 > c and x + all // 2 > r:
        return solution(x, y, n-1)
    
    if y + all // 2 <= c and x + all // 2 > r:
        answer += temp
        return solution(x, y + all//2, n-1)
    
    if y + all // 2 > c and x + all // 2 <= r:
        answer += temp * 2
        return solution(x + all//2, y, n-1)
    
    if y + all // 2 <= c and x + all // 2 <= r:
        answer += temp * 3
        return solution(x+all//2, y+all//2, n-1)
        

n, r, c = map(int, sys.stdin.readline().split())
answer = 0
solution(0, 0, n)

# 그래서 찾아보니까 재귀로 푼 사람이 없고 다 그냥 while 써서 해결했기에 나도 while로 풀었음...
N, r, c = map(int, input().split())
cnt = 0

while N > 1:
    temp = (2 ** N) // 2
    if r < temp and c < temp: 
        N -= 1
        continue
    if r < temp and c >= temp: 
        cnt += temp ** 2
        c -= temp
        N -= 1
        continue
    if r >= temp and c < temp: 
        cnt += temp ** 2 * 2
        r -= temp
        N -= 1
        continue
    if r >= temp and c >= temp:
        cnt += temp ** 2 * 3
        r -= temp
        c -= temp
        N -= 1
        continue

if r == 0 and c == 0:
    print(cnt)
if r == 0 and c == 1:
    print(cnt + 1)
if r == 1 and c == 0:
    print(cnt + 2)
if r == 1 and c == 1:
    print(cnt + 3)
