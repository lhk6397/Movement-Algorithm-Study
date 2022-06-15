# https://programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    cnt = 0
    cnt_zero = 0
    rank = { 6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6 }
    for l in lottos:
        if l in win_nums:
            cnt += 1
        if l == 0:
            cnt_zero += 1

    answer = [rank[cnt+cnt_zero], rank[cnt]]
    return answer