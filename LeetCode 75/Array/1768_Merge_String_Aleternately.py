class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)

'''
How it works:
1. Initialize an empty list repr(result) to store the merged characters.
2. Use a while loop that continues as long as there are characters left in either repr(word1) or repr(word2).
3. Inside the loop, check if the current index repr(i) is within the bounds of repr(word1). If it is, append the character at that index to repr(result).
4. Similarly, check if `i` is within the bounds of `word2` and append its character if it exists.
5. Increment `i` by 1 after each iteration.
6. Finally, join the list `result` into a string and return it.
'''