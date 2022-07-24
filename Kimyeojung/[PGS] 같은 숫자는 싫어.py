def solution(arr):

    li_arr=[]
    li_arr.append(arr[0])

    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            li_arr.append(arr[i])

    return li_arr