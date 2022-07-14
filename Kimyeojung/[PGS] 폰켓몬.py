def solution(nums):
    answer = 0

    li_nums=list(nums)
    li_set=set(li_nums)

    if len(li_nums)/2<len(li_set):
        answer=len(li_nums)/2
    else:
        answer=len(li_set)

    return answer