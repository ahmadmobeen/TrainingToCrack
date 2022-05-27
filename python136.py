class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        twice_dict = {}
        
        for num in nums:
            
            twice_dict[num] = twice_dict[num] + 1 if num in twice_dict.keys() else 1
        for key, val in twice_dict.items():
            if twice_dict[key] == 1:
                return key
