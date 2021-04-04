
def solution(n, times):
    answer = 0
    times = sorted(times)
    min_time = 1
    max_time = n * max(times)
    #print(min_time)
    #print(max_time)
    while min_time <= max_time:
        mid_time = (max_time + min_time) // 2
        #print(mid_time)
        count = 0
        for t in times:
            count += mid_time // t
            if(count >= n):
                break

        if(count >= n):
            answer = mid_time
            max_time = mid_time - 1

        else:
            min_time = mid_time + 1


    return answer

print(solution(6,[7,10]))