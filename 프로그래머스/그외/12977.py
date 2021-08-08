def is_prime(n):

    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    cnt = 0
    for i in range(len(nums) - 2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                #print(i, j, k)
                if is_prime(nums[i]+nums[j]+nums[k]):
                    cnt += 1
    return cnt
print(solution([1,2,3,4]))