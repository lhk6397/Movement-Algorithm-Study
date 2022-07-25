import sys
n = int(sys.stdin.readline())
graph = [] 
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

w_count = 0
b_count = 0
def solution(x, y, n):
    global w_count, b_count
    color = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != graph[i][j]:
                solution(x, y, n//2)
                solution(x+n//2, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y+n//2, n//2)
                return 
    
    if color == 0:
        w_count += 1
    else:
        b_count += 1


solution(0, 0, n)
print(w_count)
print(b_count)
