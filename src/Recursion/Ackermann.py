class Solution:
    def Ackermann(self, m, n):
        if m == 0:
            return n + 1
        if m > 0 and n == 0:
            return self.Ackermann(m - 1, 1)
        return self.Ackermann(m - 1, self.Ackermann(m, n - 1))


def main():
    sol = Solution()
    print("result: ", sol.Ackermann(1, 2))


if __name__ == "__main__":
    main()