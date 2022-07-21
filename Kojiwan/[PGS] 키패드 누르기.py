def point_length(p1, p2):
    a = p2[0] - p1[0]
    b = p2[1] - p1[1]

    c = abs(a) + abs(b)
    return c

def solution(numbers, hand):
    geometry = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        0: (3, 1)
    }

    left_num = [1, 4, 7]
    right_num = [3, 6, 9]

    answer = ''
    left = (3,0)
    right = (3,2)
    for number in numbers:
        now_point = geometry[number]
        if number in left_num:
            answer += 'L'
            left = now_point
        elif number in right_num:
            answer += 'R'
            right = now_point
        else:
            ldist = point_length(left, now_point)
            rdist = point_length(right, now_point)
            if(ldist > rdist):
                answer += 'R'
                right = now_point
            elif(ldist < rdist):
                answer += 'L'
                left = now_point
            else:
                if hand == "right":
                    answer += 'R'
                    right = now_point
                else:
                    answer += 'L'
                    left = now_point
    return answer