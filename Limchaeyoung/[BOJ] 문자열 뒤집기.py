# https://www.acmicpc.net/problem/1439
s = list(map(int, input()))
cnt0 = 0 # 0으로 뒤집는 개수
cnt1 = 0 # 1으로 뒤집는 개수
if s[0]:
    cnt0 += 1
else:
    cnt1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1]:
            cnt0 += 1
        else:
            cnt1 += 1
print(min(cnt0, cnt1))
