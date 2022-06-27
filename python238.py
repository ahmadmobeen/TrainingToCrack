class Solution:
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
