class Solution:
    def reverseWords(self, s: str) -> str:
        
        result = ""
        s_list = list(s)
        list_words = []
        tmp = ""
        for i in range(len(s_list)):
            if s_list[i] == " ":

                list_words.append(tmp) if tmp != "" else tmp
                tmp = ""
                continue
            tmp += (s_list[i])
        list_words.append(tmp) if tmp != "" else tmp

        for i in range(len(list_words)-1, -1, -1):
            result += list_words[i]
            result += " " if i !=0 else ""    
        return result
            
