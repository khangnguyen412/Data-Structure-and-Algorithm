class Solution:
    def Fibonaccy(self, n):
        if n <= 2:
            return 1
        else:
            return self.Fibonaccy(n - 1) + self.Fibonaccy(n - 2)


def main():
    sol = Solution()
    print("result: ", sol.Fibonaccy(8))


if __name__ == "__main__":
    main()
