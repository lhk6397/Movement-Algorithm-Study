def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    key = [[x,y] for x in range(4) for y in range(3)]
    key.insert(0,0)
    print(key)
    for x in range(3):
        for y in range(4):
            key.append([x,y])
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            left = n
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            right = n
        else:
            if n == 0:
                n = 11
            if abs(key[n][0]-key[right][0])+abs(key[n][1]-key[right][1]) > abs(key[n][0]-key[left][0])+abs(key[n][1]-key[left][1]):
                answer += 'L'
                left = n
            elif abs(key[n][0]-key[right][0])+abs(key[n][1]-key[right][1]) < abs(key[n][0]-key[left][0])+abs(key[n][1]-key[left][1]):
                answer += 'R'
                right = n
            else:
                if hand == "left":
                    answer += 'L'
                    left = n
                else:
                    answer += 'R'
                    right = n
    return answer