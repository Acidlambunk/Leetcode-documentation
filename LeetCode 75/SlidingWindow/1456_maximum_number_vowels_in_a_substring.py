class Solution:
    def maxVowels(self, s: str, k: int) -> int:
       
        vowels = ('aiueoAIUEO')
        n = len(s_list)
        if n < k:
            return 0
        
        counter = 0
        for i in range (k):
            if s[i] in vowels:
                counter += 1
        
        max_counter = counter
        for i in range (k,n):
            if s[i - k] in vowels:
                counter -= 1
            # Add vowel coming into the window
            if s[i] in vowels:
                counter += 1

            # Update max_count if needed
            if counter > max_counter:
                max_counter = counter

        return max_counter
    
    '''how it works:
    1. Initialize a counter for vowels in the first k characters.
    2. Slide the window across the string, updating the counter by removing the vowel that is sliding out and adding the new vowel that is sliding in.
    3. Keep track of the maximum count of vowels encountered.
    4. Return the maximum count.
    '''