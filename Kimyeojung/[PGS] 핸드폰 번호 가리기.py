def solution(phone_number):
    answer = ''

    li_num=list(str(phone_number))

    for i in range(0, len(li_num)-4):
        li_num[i]='*'

    answer=''.join(li_num)

    return answer