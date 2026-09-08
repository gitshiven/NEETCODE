class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        max_streak = 0

        for i in numSet:
            if i-1 not in numSet:
                streak = 1

                while (i+streak) in numSet:
                    streak+=1
                max_streak = max(max_streak, streak)
        return max_streak