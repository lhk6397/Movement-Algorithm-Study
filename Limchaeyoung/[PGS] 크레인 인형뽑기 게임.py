# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    cnt = 0
    data = []
    print(board)
    for x in moves:
        for y in range(len(board)):
            if board[y][x-1] != 0:
                data.append(board[y][x-1])
                board[y][x-1] = 0
                if len(data) >= 2:
                    if data[-2] == data[-1]:
                        data.pop()
                        data.pop()
                        cnt += 2
                break
    return cnt