def solution(n, stations, w):
    answer = 3
    # 1<= x <= n
    # station -> 오름차
    first = len(stations)
    before = 1
    if stations[-1] + w < n:
        stations.append(n - w)
    total_station = []
    for station in stations:

        for i in range(station,before - 1,-w *2 - 1):
            total_station.append(i)
            print(i)
        print()
        before = station

    if min(total_station) - w > 1:
        total_station.append(1)
    total_station = set(total_station)

    return len(total_station) - first

print(solution(16,	[9],	2))
solution(11,[4,11],1)