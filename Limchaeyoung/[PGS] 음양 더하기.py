# https://programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    sum = 0
    for x in range(len(absolutes)):
        if signs[x]: sum += absolutes[x]
        else: sum -= absolutes[x]
    return sum