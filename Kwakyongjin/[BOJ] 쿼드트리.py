import sys

def solution(x, y, n):
    temp = graph[x][y]

    if n == 1:
        return result.append(temp)

    for i in range(x, x + n):
        for j in range(y, y + n):
            if not graph[i][j] == temp:
                return result.append('('), solution(x, y, n//2), solution(x, y+n//2, n//2), solution(x+n//2,y,n//2), solution(x+n//2,y+n//2,n//2), result.append(')')
    
    return result.append(temp)


n = int(sys.stdin.readline().rstrip())
graph = []
for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

result = []
solution(0, 0, n)
print(''.join(result))
