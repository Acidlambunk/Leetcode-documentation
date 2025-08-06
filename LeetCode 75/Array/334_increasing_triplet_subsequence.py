from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
    
'''How it works:
1. Initialize two variables `first` and `second` to infinity.
2. Iterate through each number in the list `nums`.
3. If the current number is less than or equal to `first`, update `first` to this number.
4. If the current number is greater than `first` but less than or equal to `second`, update `second` to this number.
5. If a number is found that is greater than both `first` and `second`, return `True`, indicating an increasing triplet subsequence exists.
6. If the loop completes without finding such a triplet, return `False`.
'''