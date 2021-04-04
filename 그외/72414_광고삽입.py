import datetime


def to_time(time):
    h = str(time // 3600).zfill(2)
    time = time % 3600
    m = str(time // 60).zfill(2)
    s = str(time % 60).zfill(2)

    return ':'.join([h, m, s])

def solution(play_time, adv_time, logs):
    answer = ''

    p_time_list = play_time.split(":")
    play_time_sec = int(p_time_list[0]) * 3600 + int(p_time_list[1]) * 60 + int(p_time_list[2])

    a_time_list = adv_time.split(":")
    adv_time_sec = int(a_time_list[0]) * 3600 + int(a_time_list[1]) * 60 + int(a_time_list[2])
    #print(adv_time_sec)
    log_sec = []
    for log in logs:
        log_split = log.split("-")
        start_time = log_split[0]
        end_time = log_split[1]

        s_time_list = start_time.split(":")
        s_time_sec = int(s_time_list[0]) * 3600 + int(s_time_list[1]) * 60 + int(s_time_list[2])

        e_time_list = end_time.split(":")
        e_time_sec = int(e_time_list[0]) * 3600 + int(e_time_list[1]) * 60 + int(e_time_list[2])
        log_sec.append([s_time_sec,e_time_sec])

    log_sec = sorted(log_sec)
    #print(log_sec)
    #print(play_time_sec)
    play_arr = [0] * (play_time_sec + 1)

    for log in log_sec:
        play_arr[log[0]] = play_arr[log[0]] + 1
        play_arr[log[1]] = play_arr[log[1]] - 1

    for i in range(1,len(play_arr)):
        play_arr[i] = play_arr[i] + play_arr[i-1]

    for i in range(1,len(play_arr)):
        play_arr[i] = play_arr[i] + play_arr[i-1]

    max_idx = 0
    max_play = play_arr[adv_time_sec-1]
    print(len(play_arr))
    print(adv_time_sec)
    for i in range(adv_time_sec,len(play_arr)):
        cur = play_arr[i] - play_arr[i-adv_time_sec]
        if cur > max_play:
            max_play = cur
            max_idx = i - adv_time_sec + 1

    return to_time(max_idx)


#solution("02:03:55"	,"00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
#solution("50:00:00",	"50:00:00",	["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])
print(str(datetime.timedelta(seconds=59)))
'''
"02:03:55"	"00:14:15"	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]	"01:30:59"
"99:59:59"	"25:00:00"	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]	"01:00:00"
"50:00:00"	"50:00:00"	["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]	"00:00:00"

times = []
    for i,log_s in enumerate(log_sec):
        adv_s = log_s[0]
        adv_e =log_s[0] + adv_time_sec
        time = 0
        for log_s2 in log_sec:
            if log_s2[0] <= adv_s <= log_s2[1]:
                if log_s2[0] <= adv_e <= log_s2[1]:
                    time += adv_time_sec
                elif log_s2[1] < adv_e:
                    time += log_s2[1] - adv_s
            elif adv_s < log_s2[0] and adv_e > log_s2[0] and adv_e <= log_s2[1]:
                time += adv_e - log_s2[0]
            elif adv_s < log_s2[0] and adv_e > log_s2[0] and adv_e >= log_s2[1]:
                time += log_s2[1] - log_s2[0]
        times.append([i,time])

    max_t = 0
    i_li = []
    for i in range(len(times)):
        if max_t <= times[i][1]:
            max_t = times[i][1]

    for i in range(len(times)):
        if max_t == times[i][1]:
            i_li.append(i)
    #print(times)
    tt = []

    for i in i_li:
        tt.append(log_sec[i])
    tt = sorted(tt)
    #print(tt[0][0])
    if tt[0][0] + adv_time_sec > play_time_sec:
        answer = str(datetime.timedelta(seconds=(tt[0][0]- ((tt[0][0] + adv_time_sec) - play_time_sec))))
    else:
        answer = str(datetime.timedelta(seconds=tt[0][0]))
    #print(answer)
    if len(answer) == 7:
        answer = "0"+answer


'''