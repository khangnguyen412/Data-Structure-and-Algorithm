class Solution:
    def GreatestCommonDivisor(self, p, q):
        if p % q == 0:
            return q
        else:
            return self.GreatestCommonDivisor(q, p % q)


def main():
    sol = Solution()
    print("result: ", sol.GreatestCommonDivisor(4, 7))


if __name__ == "__main__":
    main()
