def solution(num):
    answer = 0

    if num==1:
        answer=0
    else:
        for i in range(1,501):
            if num%2==0:
                num=num/2
            else:
                num=(num*3)+1

            if num!=1:
                continue
            else:
                answer=i
                break

    if num!=1:
        answer=-1

    return answer