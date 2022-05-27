class Solution(object):
    def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         s_str = str(x)
#         for i in range((len(s_str)/2)):
#             if s_str[i] != s_str[-1*(1+i)]:
#                 return False
            
#         return True
#         return str(x) == str(x)[::-1]
    
        if x < 0 or (x % 10 == 0 and  x != 0):
            return False
        
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            
            x /= 10
            
        return x == reverted_number or x == reverted_number / 10
