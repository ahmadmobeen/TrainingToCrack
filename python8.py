# https://leetcode.com/problems/string-to-integer-atoi/
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        neg_flag = 1
        sign_set = False
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        num = '0'
        i = 0
        
        def isDigit(digit):
            return True if digit in digits else False
        
        while i < len(s) and s[i] == ' ':
                i += 1
        
        if i < len(s) and s[i] == '-':
            neg_flag = -1
            i += 1
        elif  i < len(s) and s[i] == '+':
            i += 1
        
            
        while i < len(s) and isDigit(s[i]):
            num += s[i]
            i += 1
            
        if  (neg_flag * int(num)) > (2**31) - 1:
            return 2**31 - 1
        elif (neg_flag * int(num)) < -(2**31):
            return -(2**31)
        else:
            return neg_flag * int(num)
                
        
        ### Dirty and not complete
        '''
        for i in range(len(s)):
                           
            if s[i] == ' ':
                continue
            
            elif s[i] == '+':
                if sign_set:
                    return 0
                else:
                    sign_set = True
                continue
            
            elif s[i] == '-':
                if sign_set:
                    return 0
                else:
                    neg_flag = -1
                    sign_set = True
                continue

            elif not isDigit(s[i]):
                break
            num = num + (s[i])
                   
        if  (neg_flag * int(num)) > (2**31) - 1:
            return 2**31 - 1
        elif (neg_flag * int(num)) < -(2**31):
            return -(2**31)
        else:
            return neg_flag * int(num)
            
            '''
