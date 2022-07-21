def solution(s):
    answer = ''

    li=list(s)
    if li[0]=='-' or li[0]=='+':
        answer+=li[0]
        for i in range(1, len(li)):
            answer += str(li[i])
    else:
        for i in range(0,len(li)):
            answer+=str(li[i])

    return int(answer)