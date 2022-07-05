# https://programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    data = list(map(int, s.split(' ')))
    return str(min(data)) + ' ' + str(max(data))