class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1

def main():
    sol = Solution()
    print("show:", sol.strStr("xadbutsad", "sad"))

if __name__ == "__main__":
    main()
