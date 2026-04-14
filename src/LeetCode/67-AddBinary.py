class Solution(object):
    def addBinary(self, a, b):
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        result = ""
        reversed_result = ""
        while i >= 0 or j >= 0 or carry != 0:
            if i >= 0:
                bit_a = int(a[i])
            else:
                bit_a = 0
            if j >= 0:
                bit_b = int(b[j])
            else:
                bit_b = 0
            total = bit_a + bit_b + carry # tính tổng (tổng các bit và carry + lại)
            bit_result = total % 2 # trả kết quả về (nếu total trên là 2,0 thì lưu "0", còn 1 thì lưu "1")
            carry = total // 2 # biến nhớ (nếu chia hết cho 2 thì ko còn nhớ, ngược lại ghi 1)
            result += str(bit_result)
            i -= 1
            j -= 1
        for x in range(len(result) - 1, -1, -1):
            reversed_result += str(result[x])
        return reversed_result


def main():
    sol = Solution()
    print("result:", sol.addBinary("11", "1"))  # 100
    print("result:", sol.addBinary("1010", "1011"))  # 10101


if __name__ == "__main__":
    main()
