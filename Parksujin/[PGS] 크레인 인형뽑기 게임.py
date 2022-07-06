def solution(board, moves):
    answer = 0
    bag = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] > 0:
                bag.append(board[j][i - 1])
                board[j][i - 1] = 0
                
                
                if len(bag) >= 2:
                    if bag[-1] == bag[-2]:
                        del bag[-1]
                        del bag[-1]
                        answer += 2
                break
    return answer
  
  # def solution(board, moves):
  #   answer = 0
  #   bag = []
    
  #   for i in moves:
  #       for j in range(len(board)):
  #           if board[j][i - 1] > 0:
  #               target = board[j][i - 1]
  #               board[j][i - 1] = 0
  #               if len(bag) >= 2 and bag[-1] == target:
  #                   bag.pop()
  #                   answer += 2
  #               else:
  #                   bag.append(target)

  #               break
  #   return answer