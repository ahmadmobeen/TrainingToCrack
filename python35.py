class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        mid = int((left + right) / 2)
        if target == nums[mid]:
            return mid

        
        while right >= left: # != nums[mid]:
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            
            mid = int((left + right) / 2)
            print(mid)
            
            # if (left - right == 1):
            #     return mid + 1
            # elif (left - right == -1):
            #     return mid
            #     break
    
        return left
