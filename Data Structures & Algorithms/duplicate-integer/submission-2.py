class Solution: 
    def hasDuplicate(sef, nums: List[int]) -> bool:
        my_set = set(nums);
        return len(my_set) != len(nums)


        