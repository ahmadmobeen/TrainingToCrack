class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Fix a number and then apply Two Sum II, which basically works on sorted array.
        A sum of two numbers in a sorted array can be increased or decreased by moving the
        pointers i.e., l, and r. If the sum is too large, decrement the r pointer, and if the 
        sum is too small, increment the l pointer.
        '''
        target = 0
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                # print(i, l, r)
                threeS = nums[i] + nums[l] + nums[r]
                if threeS > target:
                    r -= 1
                elif threeS < target:
                    l += 1
                elif threeS == target:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1  # l += 1
                    while nums[r] == nums[r + 1] and l < r: # while nums[l] == nums[l + 1] and l < r:
                    r -= 1                                  # l += 1
        return res
        # Brute force (didnt work)
        '''
        for i in range(0, len(nums) - 2, 2):
            for j in range(i + 1, len(nums) - 1, 2):            
                for k in range(j + 1, len(nums)):
                    
                    if (nums[i] + nums[j] + nums[k] == target) and (i != j) and (i != k) and (j != k):
                        res.append([nums[i], nums[j], nums[k]])
        return res'''
