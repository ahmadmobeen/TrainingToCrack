class Solution(object):
    def romanToInt(self, s):
        letters = [char for char in s]

        romandictionary= {"I": 1, "V":5, "X":10, "L":50 , "C":100, "D":500, "M": 1000, "IV": 4, "IX":9, "XL": 40, "XC": 90, "CD":400, "CM":900 }

        i = 0
        number = 0
        while i < len(letters):
            if i == len(letters)-1:
                number += romandictionary.get(letters[i])
            else:
                if romandictionary.get(letters[i]) >= romandictionary.get(letters[i+1]):
                    number += romandictionary.get(letters[i])
                else:
                    number += romandictionary.get(str(letters[i]) + str(letters[i+1]))
                    i+=1
            i+=1

            
        return number
