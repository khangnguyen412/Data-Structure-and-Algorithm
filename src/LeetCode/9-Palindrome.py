class Solution(object):
    def reverse(self, x, reversed):
        if x == 0:
            return reversed
        last_digit = x % 10
        new_reversed = reversed * 10 + last_digit
        return self.reverse(x // 10, new_reversed)

    def isPalindrome(self, x):
        temp = ""
        if x < 0:
            return False
        else:
            temp = self.reverse(x, 0)
            return temp == x

def main():
    sol = Solution()
    print(sol.isPalindrome(123))

if __name__ == "__main__":
    main()