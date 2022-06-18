# https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    cnt = 0
    d.sort()
    for x in d:
        budget -= x
        if budget >= 0:
            cnt += 1
        else:
            break
    return cnt