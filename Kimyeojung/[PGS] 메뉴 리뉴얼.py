from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        arr=[]
        for menu in orders:
            com=combinations(sorted(menu),i)
            arr+=com
        count=Counter(arr)
        if len(count)!=0 and max(count.values())!=1:
            for j in count:
                if count[j]==max(count.values()):
                    answer+=["".join(j)]

    return sorted(answer)