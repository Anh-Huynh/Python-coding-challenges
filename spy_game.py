# Write a function that takes in a list of integers and returns True if it contains 007 in order

# option 1
# def spy_game(nums):
#     if 0 in nums and 7 in nums: 
#         spy_list = nums[nums.index(0)+1 : nums.index(7)]
#         return 0 in spy_list    
#     return False

# option 2
def spy_name(nums): 
    spy_list = [0,0,7]
    for num in nums:
        if spy_list[0] == num:
            spy_list.pop(0)
    return len(spy_list) == 0