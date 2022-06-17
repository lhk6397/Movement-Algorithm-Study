# https://programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    answer = []
    for x in range(len(arr1)):
        plus = [(arr1[x])[i] + arr2[x][i] for i in range(len(arr1[x]))]
        answer.append(plus)
    return answer