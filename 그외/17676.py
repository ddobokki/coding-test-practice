# #https://programmers.co.kr/learn/courses/30/lessons/17676
#
# #추석트래픽
#
# import datetime
#
# def solution(lines):
#     answer = 0
#     process_list = []
#     for line in lines:
#         ymd = datetime.datetime.strptime(line[0:10], "%Y-%m-%d")
#         hour = line[11:13]
#         min = line[14:16]
#         sec = line[17:19]
#         ms = line[20:23] + "000"
#         process_s = line[24:25]
#         process_ms = line[27:-1] + "000"
#
#         d1 = datetime.datetime(ymd.year, ymd.month, ymd.day, int(hour), int(min), int(sec), int(ms))
#         d2 = datetime.datetime(ymd.year, ymd.month, ymd.day, 0, 0, int(process_s), int(process_ms))
#         start = d1 - d2
#         end = d1 - datetime.datetime(ymd.year,ymd.month,ymd.day)
#         process_list.append([start, end])
#
#     print(process_list)
#     cnt_list = []
#
#     start = process_list[0][0]
#     d_sec = datetime.timedelta(seconds=1)
#     end = start + d_sec
#     loop = 0
#     while(end < process_list[-1][1]):
#         cnt = 0
#         loop += 1
#         for i in range(len(process_list)):
#             if(end < process_list[i][0] or start >= process_list[i][1]):
#                 continue
#             else:
#                 cnt +=1
#             cnt_list.append(cnt)
#         start = end
#         end = end + d_sec
# 
#     print(cnt_list)
#     print(loop)
#     return answer
#
# lines = [
# "2016-09-15 20:59:57.421 0.351s",
# "2016-09-15 20:59:58.233 1.181s",
# "2016-09-15 20:59:58.299 0.8s",
# "2016-09-15 20:59:58.688 1.041s",
# "2016-09-15 20:59:59.591 1.412s",
# "2016-09-15 21:00:00.464 1.466s",
# "2016-09-15 21:00:00.741 1.581s",
# "2016-09-15 21:00:00.748 2.31s",
# "2016-09-15 21:00:00.966 0.381s",
# "2016-09-15 21:00:02.066 2.62s"
# ]
#
# # lines = [
# # "2016-09-15 01:00:04.001 2.0s",
# # "2016-09-15 01:00:07.000 2s"
# # ]
#
# solution(lines)
