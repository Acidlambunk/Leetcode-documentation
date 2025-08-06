class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        left = 0
        right = len(s_list) - 1

        while left < right:
            while left < right and s_list[left] not in vowels:
                left += 1
            while right > left and s_list[right] not in vowels:
                right -= 1
        
            s_list[left], s_list[right] = s_list[right], s_list[left]
            
            left += 1
            
            right -= 1
        return "".join(s_list)

'''How it works:
1. Create a set of vowels for quick lookup.
2. Convert the string `s` into a list `s_list` to allow modifications.
3. Initialize two pointers: `left` at the start and `right` at the end of the list.
4. Use a while loop to iterate until the two pointers meet.
5. Move the `left` pointer to the right until it finds a vowel.
6. Move the `right` pointer to the left until it finds a vowel.
7. Swap the vowels at the `left` and `right` pointers.
8. Move both pointers inward and repeat until they meet.
9. Finally, join the list back into a string and return it.
'''