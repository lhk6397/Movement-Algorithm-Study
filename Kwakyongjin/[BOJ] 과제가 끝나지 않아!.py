import sys
input = sys.stdin.readline

n = int(input())
tmp = [list(input().rstrip().split()) for _ in range(n)]
score = []
lst_time = []

for i in range(n):
    if tmp[i][0] == '0':
        if lst_time:
            lst_time[-1][0] -= 1

            if lst_time[-1][0] == 0:
                end_t, end_a = lst_time.pop()
                score.append(end_a)

    else:
        a = int(tmp[i][1])
        t = int(tmp[i][2])
        lst_time.append([t-1,a])

        if lst_time[-1][0] == 0:
            end_t, end_a = lst_time.pop()
            score.append(end_a)

print(sum(score))
