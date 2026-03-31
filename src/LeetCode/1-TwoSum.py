class Solution(object):
    def twoSum(self, nums, target):
        temp = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in temp:
                return [i, temp[complement]]
            else:
                temp[nums[i]] = i

def main():
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))

if __name__ == "__main__":
    main()