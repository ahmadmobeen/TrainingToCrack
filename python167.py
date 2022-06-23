class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Take benefit of sorted input array
        # Two pointers technique
        
        l, r = 0, len(numbers) - 1
        diff = 0
        while l < r:
            
            s = numbers[l] + numbers[r]
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            elif s == target:
                return [l + 1, r + 1]
            
            
        
        # O(N) - Exactly the same solution as of the original Two Sum Problem just be mindful of the return                     sequence of indices.
        '''
        mp = {}
        for i in range(len(numbers)):
            need = target - numbers[i]
            if need in mp:
                return [mp[need] + 1, i + 1]
            else:
                mp[numbers[i]] = i
        '''
        
