# 1,4,7 => 왼손 / 3,6,9 => 오른손
# 2,5,8,0 => 현재에서 가까운 손, 만약 거리 같다면 오른손잡이 = 오른손, 왼손잡이 = 왼손


def solution(numbers, hand):
    answer = ''
    keypad = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0),
              8:(2,1), 9:(2,2), 0:(3,1), '*':(3,0), '#':(3,2)}
    left_hand = '*'
    right_hand = '#'

    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            left_hand = i
        elif i in [3, 6, 9]:
            answer += 'R'
            right_hand = i
        else:
            ldistance = abs(keypad[i][0] - keypad[left_hand][0]) + abs(keypad[i][1] - keypad[left_hand][1])
            rdistance = abs(keypad[i][0] - keypad[right_hand][0]) + abs(keypad[i][1] - keypad[right_hand][1])
            if ldistance > rdistance:
                answer += 'R'
                right_hand = i
            elif ldistance < rdistance:
                answer += 'L'
                left_hand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    left_hand = i
                else:
                    answer += 'R'
                    right_hand = i

    return answer



