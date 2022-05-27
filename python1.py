class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        
# #         for i, num in enumerate(nums):
# #             for j, num2 in enumerate(nums):
# #                 if num + num2 == target and i != j:
                    
# #                     return [i,j]
                
#         # nums.sort() it will mess up the indices
                
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
            
#         # for i in range(len(nums)):
#         #     nums[i]+nums[]
