class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            prevMap = {}
            for j in range(i + 1, len(nums)):
                diff = target - nums[j]
                if diff in prevMap:
                    triplet = [nums[i], diff, nums[j]]
                    if triplet not in res:
                        res.append(triplet)
                prevMap[nums[j]] = j
        return res

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return None