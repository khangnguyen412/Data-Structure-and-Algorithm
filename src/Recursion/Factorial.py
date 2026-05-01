class Solution:
    def Factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.Factorial(n - 1)


def main():
    sol = Solution()
    print("result: ", sol.Factorial(5))


if __name__ == "__main__":
    main()
