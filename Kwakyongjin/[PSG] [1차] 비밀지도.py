def solution(n, arr1, arr2):
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        arr1[i] = format(arr1[i], 'b')
        arr2[i] = format(arr2[i], 'b')
        while True:
            if len(arr1[i]) != n:
                arr1[i] = '0' + arr1[i]
            
            if len(arr2[i]) != n:
                arr2[i] = '0' + arr2[i]
            
            if len(arr1[i]) + len(arr2[i]) == 2*n:
                break
    
    for i in range(n):
        arr1[i] = list(arr1[i])
        arr2[i] = list(arr2[i])
    

    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0':
                answer[i][j] = ' '
            else:
                answer[i][j] = '#'
    
    for i in range(n):
        answer[i] = ''.join(answer[i])
    
    return answer
