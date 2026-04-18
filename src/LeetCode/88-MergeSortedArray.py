class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(len(nums1) - 1, -1, -1):
            if n == 0:
                break
            if m == 0:
                nums1[i] = nums2[n - 1]
                n -= 1
                continue
            if nums1[m - 1] < nums2[n - 1]:
                nums1[i] = nums2[n - 1]
                n -= 1
            else:
                nums1[i] = nums1[m - 1]
                m -= 1
        return nums1


def main():
    sol = Solution()
    print("result:", sol.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))  # [1,2,2,3,5,6]
    print("result:", sol.merge([1], 1, [], 0))  # [1]
    print("result:", sol.merge([0], 0, [1], 1))  # [0]


if __name__ == "__main__":
    main()
