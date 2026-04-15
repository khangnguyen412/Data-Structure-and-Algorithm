class Solution(object):
    def mySqrt(self, x):
        if x < 2: 
            return x
        i = 1
        while i * i <= x:
            i += 1
        return i - 1

def main():
    sol = Solution()
    print("result:", sol.mySqrt(2))  # 1
    print("result:", sol.mySqrt(4))  # 2
    print("result:", sol.mySqrt(8))  # 2


if __name__ == "__main__":
    main()
