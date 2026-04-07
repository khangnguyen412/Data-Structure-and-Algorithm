class Solution(object):
    # removeDuplicates(self, nums: List[int]) -> int:
    # @param nums: List[int] a list of integers sorted
    # @return: int the number of unique integers
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j


def main():
    sol = Solution()
    print(
        "remove duplicates:",
        sol.removeDuplicates([1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7]),
    )


if __name__ == "__main__":
    main()
