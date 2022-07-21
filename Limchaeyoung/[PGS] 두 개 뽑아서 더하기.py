# https://programmers.co.kr/learn/courses/30/lessons/68644
from itertools import combinations
def solution(numbers):
    answer = list(set(x+y for x,y in combinations(numbers, 2)))
    return sorted(answer)