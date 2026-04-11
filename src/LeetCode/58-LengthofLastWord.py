class Solution(object):
    def lengthOfLastWord(self, s):
        trim_s = s.strip()
        length_of_last_word = 0
        for i in range(len(trim_s) - 1, -1, -1):
            if trim_s[i] == " ":
                return length_of_last_word
            length_of_last_word += 1
        return length_of_last_word


def main():
    sol = Solution()
    print("result:", sol.lengthOfLastWord("Hello World"))  # 5
    print("result:", sol.lengthOfLastWord("   fly me   to   the moon  "))  # 4
    print("result:", sol.lengthOfLastWord("luffy is still joyboy"))  # 6
    print("result:", sol.lengthOfLastWord("a"))  # 1


if __name__ == "__main__":
    main()
