
def three_sum_closest(nums: list[int], target: int)-> int :
    nums.sort()
    closest_sum = float('inf')
    for i in range(len(nums) -2) :
        left = i + 1
        right = len(nums) -1
        while left < right :
            curr_sum = nums[i] + nums[left] + nums[right]
            if abs(curr_sum - target) < abs(closest_sum - target) :
                closest_sum = curr_sum
            if curr_sum < target :
                left += 1
            elif curr_sum > target :
                right -= 1
            else :
                return curr_sum
    return closest_sum


a = [4,0,5,-5,3,3,0,-4,-5]

print(three_sum_closest(a, -2))
