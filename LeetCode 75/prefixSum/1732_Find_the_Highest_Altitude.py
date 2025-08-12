class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        p = [0] * (n+1)
        
        for i in range (1, n + 1 ):
            p[i] = p[i-1] + gain[i-1]
        return max(p)

"""how it works:
1. We create a prefix sum array repr(p) where repr(p[i]) represents the altitude at the i-th point.
2. We initialize repr(p[0]) to 0, representing the starting altitude.
3. We iterate through the repr(gain) array, updating the prefix sum array repr(p) based on the gains.
4. Finally, we return the maximum value from the prefix sum array repr(p), which represents the highest altitude reached."""