#https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    g_num_of_play = dict()
    for i,j in zip(genres,plays):
        if i in g_num_of_play.keys():
            g_num_of_play[i] += j
        else:
            g_num_of_play[i] = j
    index_num_of_play = dict()
    for p,i in zip(plays,range(len(plays))):
        index_num_of_play[i] = p
    #index_num_of_play = dict(sorted(index_num_of_play.items(), reverse=True))
    g_index = dict()
    for g,p in zip(genres,index_num_of_play):
        if g in g_index.keys():
            g_index[g].append(p)
        else:
            g_index[g] = [p]
    g_num_of_play = dict(sorted(g_num_of_play.items(),key= lambda x:x[1],reverse=True))
    #print(g_num_of_play)

    #print(index_num_of_play)
    #print(g_index)

    for g in g_num_of_play.keys():
        temp_list = []
        for i in g_index[g]:
            temp_list.append((i,index_num_of_play[i]))
        temp_dict = dict(temp_list)
        #print(temp_dict)
        temp_dict = dict(sorted(temp_dict.items(),key= lambda x:x[1],reverse=True))
        temp_list = list(temp_dict.keys())
        #print(temp_list)
        for k in range(len(temp_list)):
            if(k > 1):
                break
            answer.append(temp_list[k])
    return answer

'''
변수명 날잡고 바꾸기

'''