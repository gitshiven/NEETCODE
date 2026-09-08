class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set()
        for i in nums:
            my_set.add(i)
        
        sorted_my_set = sorted(my_set)
        if not nums:
            return 0
        result = [nums[0]]
        max_length = 1
        for i in range(1,len(sorted_my_set)):
            if (sorted_my_set[i] == sorted_my_set[i-1] + 1):
                result.append(sorted_my_set[i])
            else:
                max_length = max(max_length, len(result))
                result = [sorted_my_set[i]]

        return max(max_length, len(result))
            


