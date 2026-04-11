class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

def main():
    sol = Solution()
    print("result:", sol.searchInsert([1,3,5,6], 5)) # 2
    print("result:", sol.searchInsert([1,3,5,6], 2)) # 1

if __name__ == "__main__":
    main()
