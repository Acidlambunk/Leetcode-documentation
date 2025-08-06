class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):

            if flowerbed[i] == 0:

                left_empty = (i == 0) or (flowerbed[i - 1] == 0)

                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1
                    if n <= 0:
                        return True

        return n<= 0
        
'''How it works:
1. Iterate through each position in the `flowerbed`.
2. For each position, check if it is empty (`flowerbed[i] == 0`).
3. Check if the left and right positions are also empty or out of bounds.
4. If both conditions are satisfied, place a flower at that position (`flowerbed[i] = 1`) and decrement `n`.
5. If `n` reaches zero, return `True`, indicating all flowers can be placed.
6. If the loop completes and `n` is still greater than zero, return `False`.
'''