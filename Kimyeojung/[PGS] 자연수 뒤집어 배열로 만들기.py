def solution(n):
    answer = []

    n=str(n)
    li_n=list(n)

    for i in range(0, len(li_n)):
        answer.append(int(li_n[len(li_n)-i-1]))

    return answer