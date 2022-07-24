def solution(s):
    answer = []

    li=list(s)
    big=[]
    small=[]

    for i in range(len(li)):
        if 'a'<=str(li[i])<='z':
            small.append(str(li[i]))
        elif 'A'<=str(li[i])<='Z':
            big.append(str(li[i]))

    big.sort(reverse=True)
    small.sort(reverse=True)

    answer=list(small)+list(big)
    answer1=''.join(answer)

    return answer1