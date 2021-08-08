def solution(N, stages):
    answer = []
    for i in range(1,N+1):

        challenger = 0
        fail = 0
        fail_l = []
        for user, stage in enumerate(stages):
            if i > stage:
                continue
            if i <= stage:
                challenger += 1
            if i == stage:
                fail += 1
                fail_l.append(stage)
        if challenger != 0:
            answer.append((i, fail / challenger))
        else:
            answer.append((i,0))

    answer.sort(key=lambda x:(x[1],-x[0]),reverse=True)
    #print(answer)
    answer = list(map(lambda x:x[0],answer))
    #print(answer)
    return answer

solution(5,	[2, 1, 2, 6, 2, 4, 3, 3])
solution(4,	[4,4,4,4,4])