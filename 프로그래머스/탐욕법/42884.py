def solution(routes):

    routes = sorted(routes,key=lambda x:x[0])
    camera = [routes[0]]
    for i,r in enumerate(routes):
        if camera[-1][1] >= r[0]:
            camera[-1] = [r[0],min(camera[-1][1],r[1])]
        else:
            camera.append(r)
    return len(camera)

solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]])
print(solution([[-2,-1], [1,2],[-3,0]])) #2
print(solution([[0,0],])) #1
print(solution([[0,1], [0,1], [1,2]])) #1
print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
# 배열을 만들어 체크해보자
