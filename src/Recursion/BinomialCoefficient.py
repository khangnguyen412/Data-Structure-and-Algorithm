class Solution:
    def BinomialCoefficient(self, n, k):
        if k == 0 or k == n:
            return 1
        if k > 0 and k < n:
            return self.BinomialCoefficient(n - 1, k - 1) + self.BinomialCoefficient(n - 1, k)
        return False


def main():
    sol = Solution()
    print("result: ", sol.BinomialCoefficient(5, 3))


if __name__ == "__main__":
    main()
