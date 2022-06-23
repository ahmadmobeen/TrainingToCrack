class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Optimal O(N)
        left, right = 0, len(height) - 1
        res = 0
        while left < right:

            h = (min(height[left], height[right]))
            w = right - left

            area = h * w
            res = max(res, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
        
        
        
        ### Brture Force O(N^2)
        
        '''max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                
                h = (min(height[i], height[j]))
                w = j - i
                
                area = h * w
                if area > max_area:
                    max_area = area
                    
        return max(area, max_area)'''
