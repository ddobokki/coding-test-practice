def solution(dirs):
    answer = 0
    x = 0
    y = 0
    visit = set()

    for i in range(0, len(dirs)):
        if dirs[i] == "U" and x < 5:
            x = x + 1
            if ((x-1, y), (x, y)) in visit:
                pass
            else:
                visit.add(((x-1, y), (x, y)))
        elif dirs[i] == "D" and x > -5:
            x = x - 1
            if((x, y), (x+1, y)) in visit:
                pass
            else:
                visit.add(((x, y), (x+1, y)))
        elif dirs[i] == "L" and y > -5:
            y = y - 1
            if((x, y), (x, y+1)) in visit:
                pass
            else:
                visit.add(((x, y), (x, y+1)))
        elif dirs[i] == "R" and y < 5:
            y = y + 1
            if((x, y-1), (x, y)) in visit:
                pass
            else:
                visit.add(((x, y-1), (x, y)))
        answer = len(visit)
    return answer