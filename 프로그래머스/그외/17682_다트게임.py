def split_score(dartResult):
    idx = 0
    scores = []
    while idx < len(dartResult):
        if dartResult[idx].isdigit():
            score_s = ''
            while dartResult[idx].isdigit():
                score_s += dartResult[idx]
                idx += 1
            while not dartResult[idx].isdigit():
                score_s += dartResult[idx]
                idx += 1
                if idx > len(dartResult) - 1:
                    break
            scores.append(score_s)
    return scores

def solution(dartResult):
    answer = 0

    scores = split_score(dartResult)

    total = []
    for i,score in enumerate(scores):
        idx = 0
        num = ''
        while score[idx].isdigit():
            num += score[idx]
            idx += 1
        num = int(num)

        if score[idx] == 'S':
            num = num
        elif score[idx] == 'D':
            num = num**2
        elif score[idx] == 'T':
            num = num**3
        total.append(num)

    for i,score in enumerate(scores):
        if '*' in score:
            for j in range(i,i-2,-1):
                if j < 0:
                    break
                total[j] = 2*total[j]
        if '#' in score:
            total[i] = -1 * total[i]

    return sum(total)

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S3T*"))