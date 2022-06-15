# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []

    arr1 = changeBinaryArr(arr1, n)
    arr2 = changeBinaryArr(arr2, n)
    
    for i in range(n):
        row_str = []
        for j in range(n):
            row_str.append('#' if int(arr1[i][j]) or int(arr2[i][j]) else ' ')
        answer.append("".join(s for s in row_str))
    return answer

def changeBinaryArr(arr, n):
    bin_str = [bin(i) for i in arr]
    bin_str = [i.replace("0b", "") for i in bin_str]
    bin_arr = [list(i) for i in bin_str]
    for element in bin_arr:
        while(len(element) < n):
            element.insert(0, '0')
    return bin_arr