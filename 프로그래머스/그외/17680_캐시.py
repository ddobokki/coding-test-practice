#https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    answer = 0
    cache = [] #캐시

    for city in cities: # 도시 리스트를 순회
        city = city.lower() # 소문자 변환
        if city in cache: # 처리하려는 도시가 이미 캐시에 있으면
            answer += 1 # cache hit, 1초
            cache[cache.index(city)],cache[-1] = cache[-1], cache[cache.index(city)]
            # 캐시내의 사용된 데이터를 가장 마지막 인덱스로 옮긴다.
        else:
            answer += 5 # 캐시내에 없으면 5초 추가
            if cacheSize > 0: # 캐시 사이즈가 0보다 크고
                if len(cache) == cacheSize: # 캐시가 꽉차있다면
                    cache.pop(0) # 가장 사용 안된 데이터를 pop 해준다.
                    cache.append(city) # 새로 들어온 데이터를 캐시에 넣어준다.
                else: # 사이즈에 여유가 있으면
                    cache.append(city) # 캐시에 넣어준다
    return answer


