class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        seen = set()
        for i in range(0,n):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
