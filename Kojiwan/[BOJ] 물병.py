# import sys
# arr = [1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
# n, k = map(int, sys.stdin.readline().split())

# N = n
# result = 0
# for _ in range(k-1):
#   if arr == 1:
#     break
#   for j in range(len(arr)):
#     if arr[j] < n:
#       n -= arr[j]
#       break
# for i in range(len(arr)):
#   if arr[i] < n:
#     result = arr[i-1] - n
#     break

# print(result)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

answer = 0
while bin(N).count('1') > K:
    answer += 2 ** (bin(N)[::-1].index('1'))
    N += 2 ** (bin(N)[::-1].index('1'))
print(answer)
# 어떤 수에서 그 수보다 작지만 가장 큰 2의 제곱수를 뺌
# i가 k가 될 때까지 반복, but 나눠지는 수가 1이 되면 break
# for문 빠져나왔을 때 마지막 값을 그 값보다 큰 최소의 2의 제곱수로 만들기위한 수 출력
# 524288 475712
# 524288 262144 213568
# 524288 262144 131072 82496
# 524288 262144 131072 65536 (16960 + 15808)

