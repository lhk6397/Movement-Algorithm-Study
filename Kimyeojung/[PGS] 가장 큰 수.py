def solution(numbers):
    answer = ''
    num=[]
    for i in numbers:
        num.append(str(i))

    num.sort(key=lambda x: x*3, reverse=True)
    answer=str(int(''.join(num)))

    return answer