class Solution:
    temp_arr = []
    n = 3

    def Permutation(self, k):
        if k == self.n:
            return print(self.temp_arr)
        for i in range(self.n):
            if str(i + 1) not in self.temp_arr:
                self.temp_arr.append(str(i + 1))
                self.Permutation(k + 1)
                self.temp_arr.pop()


def main():
    sol = Solution()
    print("result: ", sol.Permutation(0))


if __name__ == "__main__":
    main()