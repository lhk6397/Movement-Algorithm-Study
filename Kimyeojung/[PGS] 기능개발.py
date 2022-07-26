def solution(progresses, speeds):
    answer = []
    day=[]
    li_pro=list(progresses)
    li_speeds=list(speeds)

    for i in range(len(progresses)):
        for j in range(1, 101):
            if int(100-int(li_pro[i]))<=li_speeds[i]*j:
                day.append(int(j))
                break

    index=0

    for i in range(len(day)):
        if day[index]<day[i]:
            answer.append(i-index)
            index=i

    answer.append(len(day)-index)

    return answer