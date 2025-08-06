class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        i = 0
        while i < len(chars):
            char = chars[i]
            count = 0
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1
            chars[write] = char
            write += 1

            
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
    
'''How it works:
1. Initialize `write` to 0, which will track the position to write the compressed characters.
2. Use a while loop to iterate through the `chars` list.
3. For each character, count how many times it appears consecutively.
4. Write the character at the `write` position and increment `write`.
5. If the count is greater than 1, convert the count to a string and write each digit to the `chars` list.
6. Return the length of the compressed list, which is stored in `write`.
'''