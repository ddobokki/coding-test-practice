def solution(numbers, hand):
    answer = ''
    cur_left = '*'
    cur_right = '#'
    index_l = {1:(0,0),4:(0,1),7:(0,2),'*':(0,3),2:(1,0),5:(1,1),8:(1,2),0:(1,3)}
    index_r = {3:(2,0),6:(2,1),9:(2,2),'#':(2,3),2:(1,0),5:(1,1),8:(1,2),0:(1,3)}
    center = {2:(1,0),5:(1,1),8:(1,2),0:(1,3)}

    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            cur_left = num
        elif num in [3,6,9]:
            answer += 'R'
            cur_right = num
        else:
            dist_l = abs(index_l[cur_left][0] - center[num][0]) + abs(index_l[cur_left][1] - center[num][1])
            dist_r = abs(index_r[cur_right][0] - center[num][0]) + abs(index_r[cur_right][1] - center[num][1])
            if dist_l > dist_r:
                answer += 'R'
                cur_right = num
            elif dist_l < dist_r:
                answer += 'L'
                cur_left = num
            else:
                if hand == 'right':
                    answer += 'R'
                    cur_right = num
                else:
                    answer += 'L'
                    cur_left = num
    return answer

