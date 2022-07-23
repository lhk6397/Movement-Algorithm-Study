def solution(n):

    li_n=list(str(n))
    li_n.sort(reverse=True)

    nn=''.join(li_n)

    return int(nn)