class Solution:
    def Reverse(self, string, index=0):
        if index == len(string):
            return ""
        return self.Reverse(string, index + 1) + string[index]


def main():
    sol = Solution()
    print("result: ", sol.Reverse("PASCAL"))


if __name__ == "__main__":
    main()
