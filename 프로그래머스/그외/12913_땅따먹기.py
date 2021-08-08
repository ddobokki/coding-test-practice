def solution(land):
    for i in range(1, len(land)):
        land[i][0] += max(land[i - 1][1], land[i - 1][2], land[i - 1][3])
        land[i][1] += max(land[i - 1][0], land[i - 1][2], land[i - 1][3])
        land[i][2] += max(land[i - 1][1], land[i - 1][0], land[i - 1][3])
        land[i][3] += max(land[i - 1][1], land[i - 1][2], land[i - 1][0])
    return max(land[len(land) - 1])

# 각 땅마다 가질수 있는 최대 값들을 갱신해준다.