# 맨 처음에 이중 for문을 했더니 시간초과가 나서 이중 for문을 없애보기로 했다
import sys # 시간 초과가 되어서 찾아보니까 input()보다 이게 입력 속도가 빠르다고 함

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort() # 오름차순 정렬
theta = int(sys.stdin.readline()) # x를 임계값이라 theta로 지정
count = 0 # 가능한 조합 개수
left, right = 0, n-1 

while left < right:
    if data[left] + data[right] == theta:
        count += 1
        left += 1
    elif data[left] + data[right] < theta:
        left += 1
    else:
        right -= 1

print(count)
