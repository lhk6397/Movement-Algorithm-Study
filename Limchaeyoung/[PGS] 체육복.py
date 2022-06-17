# https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for x in reserve[:]:
        if x in lost:
            del lost[lost.index(x)]
            del reserve[reserve.index(x)]
    for x in reserve:
        if x-1 in lost:
            del lost[lost.index(x-1)]
        elif x+1 in lost:
            del lost[lost.index(x+1)]
    return n - len(lost)