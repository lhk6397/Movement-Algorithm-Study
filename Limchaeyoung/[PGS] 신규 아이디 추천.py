# https://programmers.co.kr/learn/courses/30/lessons/72410
import re
def solution(new_id):
    new_id = new_id.lower()  # 소문자 치환
    new_id = re.sub('[^a-z0-9\-_.]', '', new_id)  # -_.을 제외한 특수문자 제거
    new_id = list(new_id)
    for x in range(len(new_id) - 1):  # .이 연속으로 나오면 하나의 .의로 치환
        for y in range(x + 1, len(new_id)):
            if new_id[x] == '.':
                if new_id[y] == '.':
                    new_id[y] = ''
                else:
                    break

    if new_id[0] == '.':  # 시작이 .일시 제거
        del new_id[0]
    if len(new_id) != 0:
        if new_id[-1] == '.':  # 끝이 .일시 제거
            del new_id[len(new_id) - 1]
    new_id = ''.join(new_id)

    if len(new_id) == 0:  # new_id가 빈 문자열일시 a 추가
        new_id += 'a'

    new_id = list(new_id)
    if len(new_id) >= 16:  # new_id가 16자 이상이면 15자만 남기기
        new_id = new_id[:15]
    if len(new_id) != 0:
        if new_id[-1] == '.':  # 끝이 .일시 제거
            del new_id[len(new_id) - 1]
    new_id = ''.join(new_id)

    while len(new_id) <=2:
        new_id += new_id[-1]
    return new_id
