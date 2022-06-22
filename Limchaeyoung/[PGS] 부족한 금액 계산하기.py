# https://programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    money -= price*(count*(count+1)//2)
    return 0 if money>=0 else -money # return max(-money, 0)