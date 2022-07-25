import sys
n = int(sys.stdin.readline())
graph = [] 
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

a_count = 0
b_count = 0
c_count = 0
def solution(x, y, n):
    global a_count, b_count, c_count
    color = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != graph[i][j]:
                solution(x, y, n//3)
                solution(x+n//3, y, n//3)
                solution(x+2*(n//3), y, n//3)
                solution(x, y+n//3, n//3)
                solution(x+n//3, y+n//3, n//3)
                solution(x+2*(n//3), y+n//3, n//3)
                solution(x, y+2*(n//3), n//3)
                solution(x+n//3, y+2*(n//3), n//3)
                solution(x+2*(n//3), y+2*(n//3), n//3)
                return 
    
    if color == -1:
        a_count += 1
    if color == 0:
        b_count += 1
    if color == 1:
        c_count += 1


solution(0, 0, n)
print(a_count)
print(b_count)
print(c_count)
