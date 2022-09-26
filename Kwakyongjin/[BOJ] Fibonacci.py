array = [0, 1]
p = 10000 // 10 * 15

for i in range(2, p):
    array.append(array[i-1] + array[i-2])
    array[i] %= 10000

n = int(input())
while n != -1:
    print(array[n%p])
    n = int(input())
