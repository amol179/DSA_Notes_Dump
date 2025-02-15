class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_good = 0
        n = len(nums)
        for i in range(n):
            left = i - k
            right = i + k
            is_good = True
            if left >= 0:
                if nums[i] <= nums[left]:
                    is_good = False
            if right < n:
                if nums[i] <= nums[right]:
                    is_good = False
            if is_good:
                sum_good += nums[i]
        return sum_good