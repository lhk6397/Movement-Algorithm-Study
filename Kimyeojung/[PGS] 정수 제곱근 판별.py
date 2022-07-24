def solution(n):
    answer = 0

    i=n**0.5

    if i==int(i):
        answer=(i+1)**2
    else:
        answer=-1

    return answer