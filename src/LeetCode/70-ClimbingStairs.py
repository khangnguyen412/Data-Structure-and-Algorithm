class Solution(object):
    def climbStairs(self, n):
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2 , n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


def main():
    sol = Solution()
    print("result:", sol.climbStairs(2))  # 2
    print("result:", sol.climbStairs(3))  # 3
    print("result:", sol.climbStairs(44))  # 3


if __name__ == "__main__":
    main()
