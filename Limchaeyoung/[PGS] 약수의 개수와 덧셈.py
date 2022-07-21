# https://programmers.co.kr/learn/courses/30/lessons/77884
def solution(left, right):
    sum = 0
    for x in range(left, right+1):
        if divisor(x):
            sum += x
        else:
            sum -= x
    return sum

def divisor(num):
    cnt = 1
    for x in range(1, num):
        if num % x == 0:
            cnt += 1
        if num == 1:
            break
    return 1 if cnt%2 == 0 else 0

# 약수가 홀수인 모든 수는 제곱수
# if int(num**0.5) == num**0.5:
#     sum -= num
# else:
#     sum += num