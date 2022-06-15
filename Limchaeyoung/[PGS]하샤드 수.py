# https://programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    k = 0
    n = str(x)
    for i in n:
        k += int(i)
    if x % k == 0: return True
    else: return False