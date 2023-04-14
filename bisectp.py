from bisectp import bisect_left, bisect_right
def calCountsByRange(nums, left_value, right_value):
    r_i = bisect_right(nums, right_value)
    l_i = bisect_left(nums, left_value)
    print(r_i,l_i)
    return r_i - l_i
nums = [-1, -3, 5, 5, 4, 7, 1, 7, 2, 5, 6]
# 5 ~ 7 을 갖는 요소의 개수 구하기
nums.sort()  # 정렬은 필수
print(nums)
print(calCountsByRange(nums, 5, 7))