import sys
input = sys.stdin.readline

n, k = map(int, input().split())
order = list(map(int, input().split()))
on = []
current = 0
cnt = 0

while current < k:
    if not on:
        on.append(order[current])
        current += 1
        continue

    elif order[current] in on:
        current += 1
        continue

    elif len(on) != n:
        on.append(order[current])
        current += 1
        continue

    else:
        tmp = False
        tmp_num = 0
        for el in on:
            if not el in order[current+1:]:
                tmp = True
                tmp_num = el
        
        if tmp:
            on.remove(tmp_num)
            on.append(order[current])
            cnt += 1
            current += 1
            
            continue

        else:

            index_lst = []
            for el in on:
                index_lst.append(order.index(el, current+1, k))
        
            swp = order[max(index_lst)]
            on.remove(swp)
            on.append(order[current])
            current += 1
            cnt += 1
            continue

print(cnt)
