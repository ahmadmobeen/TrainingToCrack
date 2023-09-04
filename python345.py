class Solution:
    def reverseVowels_(self, s: str) -> str:
        vowels = [
            'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
        ]
        s = list(s)
        tmp = []
        res = ''
        for i in range(len(s)):
            if s[i] in vowels:
                tmp.append(s[i])
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = tmp.pop()
        return "".join(s)

    '''
    Try to do it in single loop
    '''
    def reverseVowels(self, s: str) -> str:
        vowels = [
            'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
        ]
        s = list(s)

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] not in vowels:
                i += 1
                continue

            if s[j] not in vowels:
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)

        # map_dic = {}
        # for i in range(len(s)):
        #     if s[i] in vowels:
        #         map_dic[i] = s[i]
        # num_vowels = len(map_dic.keys())
        # for i, key in enumerate(map_dic.keys()):
        #     s[key] = map_dic[]
        # return s

