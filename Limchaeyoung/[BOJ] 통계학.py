from collections import Counter
n = int(input())
data = []
for x in range(n):
    data.append(int(input()))
data.sort()
print(round(sum(data)/n))
print(data[n//2])
data_dic = (Counter(data))
data_cnt = sorted(data_dic, key=lambda x: data_dic[x], reverse=True)
if len(data_cnt) > 1:
    if data.count(data_cnt[0]) == data.count(data_cnt[1]):
        print(data_cnt[1])
    else:
        print(data_cnt[0])
else:
    print(data_cnt[0])
print(data[n-1]-data[0])