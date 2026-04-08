class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j



def main():
    sol = Solution()
    print(
        "remove element:",
        sol.removeElement([1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 7], 2),
    )



if __name__ == "__main__":
    main()