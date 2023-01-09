# https://school.programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    cnt = dict()
    for c in clothes:
        if c[1] in cnt: cnt[c[1]] += 1
        else: cnt[c[1]] = 1
    for i in cnt: answer *= (cnt[i]+1)
    return answer-1

'''
from collections import Counter
from functools import reduce
def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    print(list(cnt.values()))
    return reduce(lambda x, y: x*(y+1), list(cnt.values()), 1)-1
'''
