# Bài toán Add Binary
## Đề Bài
- Given two binary strings a and b, return their sum as a binary string.

Example 1:
```
Input: a = "11", b = "1"
Output: "100"
```
Example 2:
```
Input: a = "1010", b = "1011"
Output: "10101"
```

## Giải thích thuật toán bài toán Add Binary
- Cộng hai số nhị phân tương tự như cộng hai số thập phân, nhưng cơ số là 2.
- Thực hiện phép cộng từ **phải sang trái** (từ bit thấp nhất đến bit cao nhất) vì có thể có **nhớ (carry)**.
- Mỗi bước, lấy một bit từ mỗi chuỗi (nếu hết bit thì coi là 0), cộng với carry từ bước trước.
- Kết quả bit hiện tại là `(tổng) % 2`, và carry mới là `(tổng) // 2`.
- Sau khi duyệt hết các bit, nếu carry còn lại (1) thì thêm vào kết quả.
- Chuỗi kết quả thu được từ các bit tính theo thứ tự từ thấp đến cao → cần **đảo ngược** để có thứ tự đúng.

### Cách tiếp cận: 
- Dùng hai con trỏ `i`, `j` bắt đầu từ cuối hai chuỗi `a` và `b`.
- Sử dụng vòng lặp `while (i >= 0 or j >= 0 or carry != 0)` để xử lý cả trường hợp chuỗi khác độ dài và còn nhớ.
- Tại mỗi bước, lấy `bit_a = int(a[i])` nếu `i >= 0` ngược lại `bit_a = 0`, tương tự cho `bit_b`.
- Tính `total = bit_a + bit_b + carry`.
- Ghi nhận `bit_result = total % 2` và cập nhật `carry = total // 2`.
- Nối `bit_result` (dưới dạng chuỗi) vào `result`.
- Giảm `i`, `j` và tiếp tục.
- Kết thúc vòng lặp, đảo ngược `result` và trả về.

### Tóm tắt các bước thực hiện
- Khởi tạo `carry = 0`, `i = len(a)-1`, `j = len(b)-1`, `result = ""`.
- Lặp khi `i >= 0` hoặc `j >= 0` hoặc `carry != 0`:
  - Lấy `bit_a = int(a[i])` nếu `i >= 0` else `0`.
  - Lấy `bit_b = int(b[j])` nếu `j >= 0` else `0`.
  - Tính `total = bit_a + bit_b + carry`.
  - `bit_result = total % 2`, `carry = total // 2`.
  - Ghi `result += str(bit_result)`.
  - Giảm `i -= 1`, `j -= 1`.
- Đảo ngược `result` (ví dụ: `result[::-1]`).
- Trả về chuỗi đã đảo ngược.

## Độ phức tạp của thuật toán
- Time Complexity: O(max(n, m))
- Space Complexity: O(max(n, m))