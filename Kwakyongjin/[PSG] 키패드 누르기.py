def solution(numbers, hand):
    answer = []
    key_pad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              ['*', 0, '#']]
    place = {"L":'*', "R":'#'} # 손가락 위치
    for number in numbers:
        # number가 1,4,7 또는 3,6,9 이면 손가락 확정
        if number == 1 or number == 4 or number == 7:
            place["L"] = number
            answer.append("L")
        elif number == 3 or number == 6 or number == 9:
            place["R"] = number
            answer.append("R")
        else:
            # number가 2,5,8,0 일 때
            current_L = []
            current_R = []
            target = []
            for i in range(4):
                for j in range(3):
                    if number == key_pad[i][j]:
                        target.append(i)
                        target.append(j)
                    
                    if place["L"] == key_pad[i][j]:
                        current_L.append(i)
                        current_L.append(j)
                    
                    if place["R"] == key_pad[i][j]:
                        current_R.append(i)
                        current_R.append(j)

            L_length = abs(target[0] - current_L[0]) + abs(target[1] - current_L[1])
            R_length = abs(target[0] - current_R[0]) + abs(target[1] - current_R[1])

            if (L_length > R_length):
                place["R"] = number
                answer.append("R")
            
            elif(L_length < R_length):
                place["L"] = number
                answer.append("L")
            else:
                if (hand == "right"):
                    place["R"] = number
                    answer.append("R")
                else:
                    place["L"] = number
                    answer.append("L")
                    
    answer = ''.join(answer)
    return answer
