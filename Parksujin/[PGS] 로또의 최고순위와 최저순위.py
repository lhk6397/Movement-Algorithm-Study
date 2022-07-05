# lottos가 win_nums에 있다면 rank +1
# 최고순위 = lottos의 0 개수를 센 후 모두 rank에 더해줌
# 최저순위 = win_nums와 다른 수들은 겹치지 않는다.
# 1개번호 일치 & 모두 불일치 => 6위
def solution(lottos, win_nums):
    answer = []
    rank = 0
    zero = 0

    for i in lottos:
        if i != 0:
            if i in win_nums:
                rank += 1
        else:
            zero += 1

    #최고순위
    max = 7 - (rank + zero)

   # 최저순위
    min = 7 - rank

    if max > 6 : max = 6
    if min > 6 : min = 6

    return [max, min]
