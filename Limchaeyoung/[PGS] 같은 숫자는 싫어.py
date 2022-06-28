# https://programmers.co.kr/learn/courses/30/lessons/12906]
def solution(arr):
    answer = []
    for x in range(0, len(arr)-1):
        if arr[x] != arr[x+1]:
            answer.append(arr[x])
    if len(answer) == 0:
        answer.append(arr[-1])
    if len(answer) > 0:
        if answer[-1] != arr[-1]:
            answer.append(arr[-1])
    return answer