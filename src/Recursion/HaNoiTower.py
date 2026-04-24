class Solution:
    def HaNoiTower(self, n, start, mid, end):
        # print(n, start, mid, end)

        if n == 1:
            print("1 move ", start, " to ", end)
            return

        self.HaNoiTower(n - 1, start, end, mid)

        print(n, "move ", start, " to ", end)

        self.HaNoiTower(n - 1, mid, start, end)


def main():
    sol = Solution()
    print("result: ", sol.HaNoiTower(3, "A", "B", "C"))


if __name__ == "__main__":
    main()