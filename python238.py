class Solution:
    '''
    Attempted again after a year (2023 sept)
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time complexity: O(N)
        # Space complexity: O(2 * N) ~ O(N)
        len_nums = len(nums)
        res = [1] * len_nums
        pre = [1] * len_nums
        post = [1] * len_nums
        pre_prod = 1
        post_prod = 1
        for i in range(1, len_nums):
            pre_prod *= nums[i-1]
            pre[i] = pre_prod
        for i in range(len_nums-2, -1, -1):
            post_prod *= nums[i+1]
            post[i] = post_prod
        for i in range(len_nums):
            res[i] = pre[i] * post[i]
        return res
        
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Try in Space O(1)
        '''
        n = len(nums)
        ans = [1] * n
        prod = 1
        for i in range(1, n):
            prod *= nums[i-1]
            ans[i] = prod
        prod = 1
        for i in range(n-2, -1, -1):
            prod *= nums[i+1]
            ans[i] *= prod
        return ans
# ---------------------------------------------------------- #
            
'''
Did in 2022
'''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #    Time complexity: O(N) Space complexity O(1)
        n = len(nums)
        
        ans = [1] * n
        pre = post = 1
        for i in range(0, n):
            if i == 0:
                ans[i] = 1
            else:
                ans[i] = ans[i - 1] * nums[i - 1]
        print(ans)
        for i in reversed(range(n)):
            if i == n - 1:
                post *= 1
            else:
                post *= nums[i + 1]   
            ans[i] *= post
        return ans
    
        # Time complexity: O(N) Space complexity O(2 * N)
        '''
        n = len(nums)

        pre_prod = [1] * n
        post_prod = [1] * n
        ans = [1] * n
        pre = post = 1
        for i in range(0, n):
            if i == 0:
                pre_prod[i] = 1
            else:
                pre_prod[i] = pre_prod[i - 1] * nums[i - 1]      
        for i in reversed(range(n)):
            if i == n - 1:
                post_prod[i] = 1
            else:
                post_prod[i] = post_prod[i + 1] * nums[i + 1]        
        for i in range(n):
            ans[i] = pre_prod[i] * post_prod[i]

        return ans
        '''
