n = 5
answer = []
if n > 0:
    for i in range(n):
        inarr = []
        answer.append(inarr)

    print(answer)

    num = 0
    for i in range(n):
        if i == 0:
            for w in range(1,n +1):
                num = w
                answer[i].append(w)
        else:
            num += 1 
            answer[i].append(num)

    last_item = answer[-1]
    index = -1
    for i in range(n-1):
        num += 1
        answer[-1].insert(index-1, num)
        index -= 1


    data = answer[-n + 1:-1]
    data.reverse()
    for i in range(len(data)):
        for c in range(n-1):
            num += 1
            data[i].insert(c, num)
            
    data.reverse()
    answer[-n + 1:-1] = data
    print(answer)
else:
    print(None)
