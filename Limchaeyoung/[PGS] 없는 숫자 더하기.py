# https://programmers.co.kr/learn/courses/30/lessons/86051
def solution(numbers):
    answer = 0
    nlist = [0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
            nlist.remove(i)

    for i in nlist:
        answer += i
    return answer