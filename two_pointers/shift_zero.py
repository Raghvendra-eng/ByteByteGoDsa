"""
Given an array of integers, modify the array in place to move all zeros to the end while maintaining the relative order of non-zero elements.

Example:
Input: nums = [0, 1, 0, 3, 2]
Output: [1, 3, 2, 0, 0]
Intuition
This problem has three main requirements:

Move all zeros to the end of the array.
Maintain the relative order of the non-zero elements.
Perform the modification in place.
"""

    
def shift_zero(nums) :
    first = 0; length = len(nums)
    second = first + 1
    while second < length :
        while first < length and nums[first] != 0 :
            first+=1
        second = first + 1
        while second < length and nums[second] == 0:
            second += 1
        if second < length :
            nums[first], nums[second] = nums[second], nums[first]
        first+=1
    # while first < length:
    #     nums[first] = 0
    #     first += 1

nums = [0, 1, 0, 3, 2]
shift_zero(nums)
print(nums)