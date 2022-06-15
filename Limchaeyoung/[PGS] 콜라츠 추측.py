# https://programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    cnt = 0
    if num == 1: return 0
    while num != 1:
        num = num//2 if num % 2 == 0 else num*3+1
        cnt +=1
        if cnt == 500: return -1
    return cnt