class Solution(object):
    def convertRomanToInt(self, s):
        if s == "I":
            return 1
        elif s == "V":
            return 5
        elif s == "X":
            return 10
        elif s == "L":
            return 50
        elif s == "C":
            return 100
        elif s == "D":
            return 500
        elif s == "M":
            return 1000
        else:
            return 0
    def romanToInt(self, s):
        total = 0
        current = 0
        next = 0
        for i in range(len(s)):
            current = self.convertRomanToInt(s[i])
            if i+1 < len(s):
                next = self.convertRomanToInt(s[i+1])
            else:
                next = 0
            if current < next:
                total = total - current
            else:
                total += current
        return total

def main():
    sol = Solution()
    print("total:", sol.romanToInt("MCMXCIV"))

if __name__ == "__main__":
    main()