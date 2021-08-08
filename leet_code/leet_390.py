import collections
class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        arr = collections.deque(list(range(2,n+1,2)))

        is_even = False
        while len(arr) != 1:
            #print(arr)
            if is_even:
                for i in range(len(arr)):
                    remaining_num = arr.popleft()
                    if i % 2 != 0:
                        arr.append(remaining_num)
                is_even = False
            else:
                for i in range(len(arr)):
                    remaining_num = arr.pop()
                    if i % 2 != 0:
                        arr.appendleft(remaining_num)
                is_even = True
        return arr.pop()

'''
시간초과

def lastRemaining(self, n: int) -> int:
    iteration = 0 #record the iteration
    point = 1 #point to the first element in the list
    interval = 1 #record the interval between elements
    while(n>1):
        if n%2 == 1 or iteration%2==0:#if we eliminate from the left or the length of list is odd, the first element will move forward one place and the interval will double 
            point+=interval
            iteration+=1
            interval*=2
            n = n//2
        else: #if we eliminate the element from right and the length of list is even, the first element doesn't change
            iteration+=1
            interval*=2
            n = n//2
    return point

모범답

'''