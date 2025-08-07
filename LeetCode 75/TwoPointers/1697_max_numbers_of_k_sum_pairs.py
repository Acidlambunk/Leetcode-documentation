class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        counter = 0
        while left < right:
            total = nums[right] + nums[left]
            if total == k:
                left += 1
                right -=1
                counter += 1
            elif total < k:
                left+=1
            else:
                 right -= 1
        return counter

'''How it works:
1. Sort the `nums` list to facilitate the two-pointer technique.
2. Initialize two pointers: `left` at the start (0) and `right` at the end (last index) of the sorted list.
3. Initialize a counter to keep track of valid pairs found.
4. Use a while loop to iterate as long as `left` is less than `right`.
5. Calculate the sum of the elements at the two pointers (`total = nums[right] + nums[left]`).
6. If `total` equals `k`, increment both pointers and increase the counter by 1, indicating a valid pair was found.
7. If `total` is less than `k`, increment the `left` pointer to increase the sum.
8. If `total` is greater than `k`, decrement the `right` pointer to decrease the sum.
9. After exiting the loop, return the counter, which contains the number of valid pairs that sum up to `k`.
'''