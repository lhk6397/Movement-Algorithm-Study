def solution(board, moves):
    basket = []
    answer = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                basket.append(board[i][move-1])
                board[i][move-1] = 0
                if basket[-1:] == basket[-2:-1]:
                    answer += basket[-1:]
                    basket = basket[:-2]
                break
    result = len(answer)*2
    return result
