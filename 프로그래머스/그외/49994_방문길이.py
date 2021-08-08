def solution(dirs):
    x,y = 0, 0
    visit_point = {}
    length = 0
    for d in dirs:
        if d == "U":
            nx,ny = x, y + 1
        if d == "L":
            nx, ny = x - 1, y
        if d == "R":
            nx, ny = x + 1, y
        if d == "D":
            nx, ny = x, y - 1

        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue

        if not (x,y,nx,ny) in visit_point:
            visit_point[(x,y,nx,ny)] = 1
            visit_point[(nx,ny,x,y)] = 1
            length += 1
        x, y = nx, ny


    return length

solution("ULURRDLLU")
solution("LULLLLLLU")