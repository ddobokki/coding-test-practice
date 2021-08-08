import heapq
def get_min(str_time):
    time = str_time.split(':')
    return int(time[0])*60 + int(time[1])
def get_melody(str_melody):
    melody_list = []

    idx = 0
    while idx < len(str_melody):
        if idx < len(str_melody) - 1 and str_melody[idx + 1] == '#':
            melody_list.append(str_melody[idx]+str_melody[idx+1])
            idx += 2
        else:
            melody_list.append(str_melody[idx])
            idx += 1
    return melody_list

def check(m,total_m):
    m_len = len(m)
    t_len = len(total_m)

    for i in range(t_len - m_len+1):
        for j in range(m_len):
            if not m[j] == total_m[i+j]:
                break
        else:
            return True
    return False

def solution(m, musicinfos):

    find = []
    for musicinfo in musicinfos:
        start,end,name,melody = musicinfo.split(',')
        melody_time = get_min(end) - get_min(start)
        melody_list = get_melody(melody)
        total_melody = ''
        for i in range(melody_time):
            total_melody += melody_list[i % len(melody_list)]
        # print(total_melody)
        memory = get_melody(m)
        total_melody = get_melody(total_melody)
        #print(total_melody)
        # print(memory)
        if check(memory,total_melody):
            heapq.heappush(find,(-melody_time,name))

    if not find:
        return "(None)"

    answer = heapq.heappop(find)

    return answer[1]
#
# print(solution(	"ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:03,WORLD,ABCDEF","13:00,13:06,WORLD1,ABCDEF"]))
#
# print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(check(["a","b","c"],["b","b","b","a","b","c"]))