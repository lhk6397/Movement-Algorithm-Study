from itertools import combinations

def com(a,b,c):
    sum=a+b+c
    for i in range(2,sum):
        if sum%i==0:
            return False
    return True

def solution(nums):
    answer = 0

    list_nums=list(combinations(nums,3))
    for i in list_nums:
        if com(i[0], i[1], i[2]):
            answer+=1

    return answer