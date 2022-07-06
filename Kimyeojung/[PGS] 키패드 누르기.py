def pos(num, left, right, hand):

    li = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    dist_left = abs(li[num][0] - li[left][0]) + abs(li[num][1] - li[left][1])
    dist_right = abs(li[num][0] - li[right][0]) + abs(li[num][1] - li[right][1])

    if dist_left < dist_right:
        return 'L'

    elif dist_left > dist_right:
        return 'R'

    else:
        if hand == 'right':
            return 'R'

        else:
            return 'L'


def solution(nums, hand):
    answer = ''

    left = '*'
    right = '#'

    for num in nums:
        if num in [1, 4, 7]:
            answer += 'L'
            left = num

        elif num in [3, 6, 9]:
            answer += 'R'
            right = num

        else:

            mid = pos(num, left, right, hand)
            answer += mid

            if mid == 'R':
                right = num

            else:
                left = num

    return answer