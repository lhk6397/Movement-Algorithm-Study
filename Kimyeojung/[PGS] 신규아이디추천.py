def solution(new_id):
    answer = ''

    new_id=new_id.lower()

    for i in new_id:
        if i.isalnum() or i in "-_.":
            answer+=i

    while '..' in answer:
        answer=answer.replace("..", ".").strip('')

    answer=answer.strip(".")

    if answer=='':
        answer='a'

    answer=answer[0:15]
    answer=answer.strip(".")

    while len(answer)<3:
        answer+=answer[-1]

    return answer