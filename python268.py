class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # Time: O(N)
        # Space: O(1)
        sum_i = 0
        sum_nums = 0
        
        for i in range(len(nums) + 1):
            sum_i += i
            if i < len(nums):
                sum_nums += nums[i]
        return 0 if sum_nums == sum_i else sum_i - sum_nums
        
        '''
        # Time Complexity O(N * Log(N)) - sorting is log(N)
        # Space Complexity O(1)
        num = -1
        nums.sort()
        for i in range(len(nums) - 1):
            if i == 0 and len(nums) >= 1 and nums[i] + 1 != nums[i + 1]:
                return nums[i] + 1
            num = nums[i] + 1
            if num != nums[i + 1]:
                return num
        return nums[-1] + 1 if nums[0] == 0 else 0'''
