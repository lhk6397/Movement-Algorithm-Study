def solution(a, b):
    answer = 0

    li_a=list(a)
    li_b=list(b)

    for i in range(len(li_a)):
        answer+=li_a[i]*li_b[i]

    return answer