def solution(answers):
    answer=[]
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    a1=0
    b1=0
    c1=0

    for i in range(len(answers)):
        if a[i%5]==answers[i]:
            a1+=1
        if b[i%8]==answers[i]:
            b1+=1
        if c[i%10]==answers[i]:
            c1+=1

    result=[a1,b1,c1]
    re_max=max(result)

    for i in range(3):
        if re_max==result[i]:
            answer.append(i+1)

    return answer


