class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        while j < len(nums):
            nums[j] = 0
            j += 1

'''How it works:
1. Initialize a pointer `j` to track the position to write non-zero elements.
2. Iterate through the list `nums` with index `i`.
3. If the current element `nums[i]` is not zero, write it to `nums[j]` and increment `j`.
4. After processing all elements, fill the remaining positions in `nums` with zeros by setting `nums[j] = 0` until the end of the list.
5. The result is that all non-zero elements are moved to the front, and all zeros are moved to the end.
'''