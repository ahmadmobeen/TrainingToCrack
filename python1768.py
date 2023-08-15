class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""
        len1 = len(word1)
        len2 = len(word2)
        # x = len1 if len1 <= len2 else len2
        for i, letter in enumerate(word1):
            if i == len2 or i == len1:
                # merged_string += word1[i]
                break
            # if i == len1:
            #     # merged_string += word2[i]
            #     break
            merged_string += word1[i]
            merged_string += word2[i]
        if len2 > len1:
            merged_string += word2[i+1:] 
        elif len2 < len1:
            merged_string += word1[i:]
        return merged_string
