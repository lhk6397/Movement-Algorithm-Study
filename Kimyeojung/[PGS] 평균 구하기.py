def solution(arr):
    answer = 0

    li_arr=list(arr)
    for i in range(len(li_arr)):
        answer+=li_arr[i]

    return float(answer)/float(len(li_arr))