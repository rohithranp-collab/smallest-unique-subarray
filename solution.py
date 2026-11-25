class Solution(object):
    def smallestUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        base = 100003
        mod = 10**9 + 7

        power = [1] * (n + 1)
        for i in range(1, n + 1):
            power[i] = (power[i - 1] * base) % mod

        def has_unique_of_length(length):
            if length > n:
                return False

            curr_hash = 0
            for i in range(length):
                curr_hash = (curr_hash * base + nums[i]) % mod

            freq = {curr_hash: 1}
            highest_pow = power[length - 1]

            for i in range(length, n):
                outgoing = nums[i - length]
                incoming = nums[i]

                curr_hash = (curr_hash - outgoing * highest_pow) % mod
                curr_hash = (curr_hash * base + incoming) % mod

                freq[curr_hash] = freq.get(curr_hash, 0) + 1

            return any(count == 1 for count in freq.values())

        left, right = 1, n
        ans = n

        while left <= right:
            mid = (left + right) // 2
            if has_unique_of_length(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans