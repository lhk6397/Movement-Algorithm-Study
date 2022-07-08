def solution(board, moves):
    answer = 0
    bag = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] > 0:
                target = board[j][i - 1]
                board[j][i - 1] = 0
                if len(bag) >= 2 and bag[-1] == target:
                    bag.pop()
                    answer += 2
                else:
                    bag.append(target)

                break
    print(answer)
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]	)