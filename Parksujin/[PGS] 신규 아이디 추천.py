# 3~15자 사이
#소문자, 숫자, - _ . 사용가능, .는 처음과 끝 x 연속 사용 불가능
def solution(new_id):
    answer = ''

    # step1
    answer = new_id.lower()

    # step2
    special = "~!@#$%^&*()=+[{]}:?,<>/"
    for i in special:
        answer = answer.replace(i, '')


    # step3
    while '..' in answer:
        answer = answer.replace('..', '.')

    # step4
    answer = answer.strip('.')

    # step5
    if not answer:
        answer = 'a'

    # step6
    if len(answer) >= 16:
        answer = answer[0:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # step7
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]


    return answer