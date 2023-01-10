n, m = map(int, input().split())
sentence = list(map(int, input().split()))
queue = [i for i in range(1, n+1)]
cnt = 0

for i in range(m):
    queue_length = len(queue)
    queue_index = queue.index(sentence[i])
    
    if queue_index < queue_length - queue_index:
        while True:
            if queue[0] == sentence[i]:
                del queue[0]
                break

            else:
                queue.append(queue[0])
                del queue[0]
                cnt += 1
    
    else:
        while True:
            if queue[0] == sentence[i]:
                del queue[0]
                break
            
            else:
                queue.insert(0, queue[-1])
                del queue[-1]
                cnt += 1

print(cnt)
