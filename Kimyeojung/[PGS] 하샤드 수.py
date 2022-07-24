def solution(x):
    answer = True

    li_x=list(str(x))
    sum=0

    for i in range(len(li_x)):
        sum+=int(li_x[i])

    if x%sum==0:
        answer=True
    else:
        answer=False

    return answer