def solution(price, money, count):
    answer = -1
    sum_money=0

    for i in range(1, count+1):
        sum_money+=price*i

    answer=sum_money-money
    if answer<=0:
        answer=0

    return answer