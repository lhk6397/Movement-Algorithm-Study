# https://programmers.co.kr/learn/courses/30/lessons/12977
import itertools
def solution(nums):
    cnt = 0
    cb = map(sum, itertools.combinations(nums, 3))
    for x in cb:
        if minority(x):
            cnt += 1
    return cnt

def minority(num):
    for y in range(2, int(num ** 0.5) + 1):
        if num % y == 0:
            return 0
    return 1

print(solution([1,2,3,4]))