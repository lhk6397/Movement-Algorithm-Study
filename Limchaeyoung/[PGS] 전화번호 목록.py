# https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    pre = dict()
    for p in phone_book:
        for i in range(1, len(p)):
            pre[p[:i]] = 1
    for p in phone_book:
        if p in pre:
            return False
    return True