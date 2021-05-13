def solution(a):
    cnt = 0
    mid = 0

    left = 0
    left_min = a[left]
    left_min_arr = []
    while left < len(a):
        left_min = min(left_min,a[left])
        left_min_arr.append(left_min)
        left += 1

    right = len(a) - 1
    right_min = a[right]
    right_min_arr = []

    while right >= 0:
        right_min = min(right_min, a[right])
        right_min_arr.append(right_min)
        right -= 1
    right_min_arr = right_min_arr[::-1]
    # print(left_min_arr)
    # print(right_min_arr)
    while mid < len(a):
        if mid == 0 or mid == len(a) - 1:
            cnt += 1
        else:
            if left_min_arr[mid - 1] < a[mid] and right_min_arr[mid+1] < a[mid]:
                cnt += 0
            else:
                cnt += 1
        mid += 1
    return cnt

solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])