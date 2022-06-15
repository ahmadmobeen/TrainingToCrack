class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        i = 0
        track = {}
        
        for i in (range(len(nums))):
            
            if nums[i] in track.keys():
                return True
            else:
                track[nums[i]] =1
        return False
