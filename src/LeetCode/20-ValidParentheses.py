class Solution(object):
    def convert(self, s):
        if s == "(":
            return -1
        elif s == ")":
            return 1
        elif s == "{":
            return -2
        elif s == "}":
            return 2
        elif s == "[":
            return -3
        elif s == "]":
            return 3
        else:
            return False

    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            num = self.convert(s[i])
            if num < 0:
                stack.append(num)
            if num > 0:
                if len(stack) == 0:
                    return False
                if abs(num) != abs(stack[-1]):
                    return False
                stack.pop()
        return len(stack) == 0


def main():
    sol = Solution()
    print("is valid:", sol.isValid("()"))
    print("is valid:", sol.isValid("()[]{}"))
    print("is valid:", sol.isValid("(]"))
    print("is valid:", sol.isValid("([)]"))
    print("is valid:", sol.isValid("{[]"))


if __name__ == "__main__":
    main()
