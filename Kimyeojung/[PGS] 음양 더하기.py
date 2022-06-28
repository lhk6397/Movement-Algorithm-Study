def solution(absolutes, signs):
    answer = 0
    list_si=list(signs)
    list_ab=list(absolutes)

    for i in range(len(list_ab)):
        if list_si[i]==True:
            answer+=list_ab[i]
        else:
            answer-=list_ab[i]

    return answer