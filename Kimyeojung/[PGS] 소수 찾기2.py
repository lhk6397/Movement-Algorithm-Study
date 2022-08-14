from itertools import permutations

def prime(x):
    if x<2:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def solution(numbers):
    answer=0
    numbers=list(numbers)
    set_num=set()
    for i in range(len(numbers)):
        for j in list(permutations(numbers, i+1)):
            k=int(''.join(j))
            if k not in set_num:
                set_num.add(k)
                if prime(k)==True:
                    answer+=1

    return answer