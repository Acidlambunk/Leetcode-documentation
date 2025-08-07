class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
                
'''How it works:
1. Initialize two pointers `left` at the start and `right` at the end of the `height` list.
2. Set `max_area` to 0 to keep track of the maximum area found.
3. Use a while loop to iterate as long as `left` is less than `right`.
4. Calculate the height of the container as the minimum of the heights at the two pointers (`h = min(height[left], height[right])`).
5. Calculate the width of the container as the difference between the two pointers (`w = right - left`).
6. Calculate the area of the container as `area = h * w`.
7. Update `max_area` with the maximum value between the current `max_area` and the newly calculated area.
8. Move the pointer that points to the shorter height inward (increment `left` if `height[left] < height[right]`, otherwise decrement `right`).
9. After exiting the loop, return `max_area`, which contains the maximum area of water that can be contained.
'''