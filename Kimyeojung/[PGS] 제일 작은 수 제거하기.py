def solution(arr):
    answer = []
    li_arr=list(arr)

    if len(arr)==1:
        answer.append(int(-1))
    else:
        li_arr.sort(reverse=True)
        k = li_arr[len(li_arr) - 1]
        arr = list(arr)
        i = arr.index(k)
        arr.pop(i)
        answer = arr

    return answer