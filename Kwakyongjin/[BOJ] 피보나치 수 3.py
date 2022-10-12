n = int(input())
array = [0, 1]
p = 1000000 // 10 * 15

for i in range(2, p):
    array.append(array[i-1] + array[i-2])
    array[i] %= 1000000

print(array[n%p])

