# https://programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    return len(nums)/2 if len(set(nums)) > len(nums)/2 else len(set(nums))