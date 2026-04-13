class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                return digits
            if digits[i] == 9:
                digits[i] = 0
        return [1] + digits


def main():
    sol = Solution()
    print("result:", sol.plusOne([1, 2, 3]))  # [1, 2, 4]
    print("result:", sol.plusOne([9]))  # [1, 0]
    print("result:", sol.plusOne([1, 2, 9]))  # [1, 3, 0]


if __name__ == "__main__":
    main()
