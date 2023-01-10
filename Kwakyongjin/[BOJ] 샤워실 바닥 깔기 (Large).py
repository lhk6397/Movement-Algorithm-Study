def solution(size, x, y, tarX, tarY):
    global cnt
    cnt += 1
    
    if size == 2:
        for i in range(2):
            for j in range(2):
                if graph[x+i][y+j] == 0:
                    graph[x+i][y+j] = cnt

    else:
        s = size//2
        x1, y1 = x, y
        x2, y2 = x + s, y
        x3, y3 = x, y + s
        x4, y4 = x + s, y + s

        if x1 <= tarX < x2 and y1 <= tarY < y3:
            graph[x2][y4-1] = cnt
            graph[x4-1][y3] = cnt
            graph[x4][y4] = cnt
            return solution(s, x1, y1, tarX, tarY), solution(s, x2, y2, x2, y4-1), solution(s, x3, y3, x4-1, y3), solution(s, x4, y4, x4, y4)
        
        if x2 <= tarX < x + size and y2 <= tarY < y4:
            graph[x2-1][y3-1] = cnt
            graph[x4-1][y3] = cnt
            graph[x4][y4] = cnt
            return solution(s, x1, y1, x2-1, y3-1), solution(s, x2, y2, tarX, tarY), solution(s, x3, y3, x4-1, y3), solution(s, x4, y4, x4, y4)

        if x3 <= tarX < x4 and y3 <= tarY < y + size:
            graph[x2-1][y3-1] = cnt
            graph[x2][y4-1] = cnt
            graph[x4][y4] = cnt
            return solution(s, x1, y1, x2-1, y3-1), solution(s, x2, y2, x2, y4-1), solution(s, x3, y3, tarX, tarY), solution(s, x4, y4, x4, y4)

        if x4 <= tarX < x + size and y4 <= tarY < y + size:
            graph[x2-1][y3-1] = cnt
            graph[x4-1][y3] = cnt
            graph[x2][y4-1] = cnt
            return solution(s, x1, y1, x2-1, y3-1), solution(s, x2, y2, x2, y4-1), solution(s, x3, y3, x4-1, y3), solution(s, x4, y4, tarX, tarY)
    return
size = int(input())
size = 2**size
graph = [[0 for _ in range(size)] for _ in range(size)] 
tarY, tarX = map(int, input().split())
tarY -= 1
tarX = size - tarX 
graph[tarX][tarY] = -1
cnt = 0

solution(size, 0, 0, tarX, tarY)

if cnt <= 19000:
    for i in range(size):
        for j in range(size):
            print(graph[i][j], end=' ')
        print()

else:
    print(-1)
