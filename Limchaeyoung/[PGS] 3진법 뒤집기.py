import math
def solution(n):
    n3 = ''
    answer = 0
    while n:
        n3 += str(n%3)
        n //= 3
    for x in range(len(n3)):
        answer += math.pow(3, (len(n3)-x-1))*int(n3[x])
    return int(answer)

# int(x, radix): radix 진수로 표현된 문자열 x를 10진수로 변환 후 반환하는 함수
# nn == int(n3, 3)