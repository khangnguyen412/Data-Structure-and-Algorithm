class Solution(object):
    def longestCommonPrefix(self, strs):
        temp_prefix = ""
        if len(strs) == 0:
            return temp_prefix
        if len(strs[0]) == 0:
            return temp_prefix
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in range(1, len(strs)):
                if i >= len(strs[s]):
                    return temp_prefix
                if strs[s][i] != char:
                    return temp_prefix
            temp_prefix += char
        return temp_prefix


def main():
    sol = Solution()
    print("longest common prefix:", sol.longestCommonPrefix(["a"]))


if __name__ == "__main__":
    main()
