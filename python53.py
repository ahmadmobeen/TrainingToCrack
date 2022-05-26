class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        window_sum = nums[0]
        i = 1
        while i < len(nums):
            
            if window_sum + nums[i] > nums[i]:
                window_sum = window_sum + nums[i]
            
            else:
                window_sum = nums[i]
            
            max_sum = max(max_sum, window_sum)
            print(max_sum)
            i += 1
            
        return max_sum

        

        
        
        
        ######### Time Limit Exceeded
#         sum_ = 0
#         max_sum = 0
#         for i in range(len(nums)):
#             sum_ = sum_ + nums[i]
#             if i == 0:
#                 max_sum = sum_
#             elif sum_ > max_sum:
#                 max_sum = sum_

#             other_sum = 0

#             for j in range(i+1, len(nums)):
#                 other_sum =  other_sum + nums[j]
#                 if other_sum > max_sum:
#                     max_sum = other_sum
#         return max_sum
        
        
        ####### Memory Limit Exceeded
#         sum_ = 0 
#         list_sum = []
#         for i in range(len(nums)):
#             sum_ = sum_ + nums[i]
#             list_sum.append(sum_)
#             other_sum = 0

#             for j in range(i+1, len(nums)):
#                 other_sum =  other_sum + nums[j]
#                 list_sum.append(other_sum)
                
#         print(list_sum)
#         return max(list_sum)
