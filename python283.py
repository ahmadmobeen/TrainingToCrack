class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeros = 0
        j = 0
        while i < len(nums):

            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                zeros += 1


            if nums[i] != 0:
                i += 1

            last_nonzero = len(nums) - zeros
            if all(nums[:last_nonzero]):
                break
