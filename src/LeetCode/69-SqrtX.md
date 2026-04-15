# Bài toán Sqrt(x)
## Đề Bài
- Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
- You must not use any built-in exponent function or operator.
- For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
```
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
```
Example 2:
```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
```

## Giải thích thuật toán bài toán Sqrt(x)
- Bài toán yêu cầu tìm số nguyên `k` lớn nhất sao cho `k * k <= x`.  
- Phương pháp **vét cạn** (Brute Force) sẽ kiểm tra lần lượt các số nguyên bắt đầu từ `1`, tăng dần cho đến khi tìm được số đầu tiên có bình phương **vượt quá** `x`. 
- Số nguyên liền trước đó chính là đáp án cần tìm.
- Để tránh lỗi **tràn bộ nhớ** (Memory Limit Exceeded) khi dùng `range()` tạo danh sách lớn trong một số môi trường Python, ta sử dụng vòng lặp **`while`** với biến đếm tự tăng.

### Cách tiếp cận: 
- **Duyệt tuần tự tăng dần:** Bắt đầu từ `i = 1`, kiểm tra điều kiện `i * i <= x`.
- **Cập nhật biến đếm:** Nếu điều kiện đúng, tăng `i` lên `1` và tiếp tục.
- **Dừng và trả kết quả:** Khi gặp `i * i > x`, vòng lặp kết thúc. Kết quả cần trả về là `i - 1` (số nguyên lớn nhất thỏa mãn bình phương không quá `x`).
- **Xử lý riêng trường hợp đặc biệt:** Với `x = 0` hoặc `x = 1`, đáp án chính là `x`.

### Tóm tắt các bước thực hiện
1. **Kiểm tra biên:** Nếu `x == 0` hoặc `x == 1`, trả về `x`.
2. **Khởi tạo:** `i = 1`.
3. **Lặp:** Trong khi `i * i <= x`:
    - Tăng `i` lên `1` (`i = i + 1`).
4. **Kết thúc:** Trả về `i - 1`.

## Độ phức tạp của thuật toán
- Time Complexity: **O(√x)**  
    - Vòng lặp chạy từ `1` đến `⌊√x⌋ + 1`, tức tối đa khoảng `√x` lần lặp.  
    - Với giới hạn `x` thông thường (`x ≤ 2³¹ - 1`), số vòng lặp tối đa chỉ ~46.340, hoàn toàn khả thi trong thời gian cho phép.
- Space Complexity: **O(1)**  
    - Thuật toán chỉ sử dụng một vài biến phụ trợ (`i`, `x`), không cấp phát thêm bộ nhớ tỉ lệ theo kích thước đầu vào.
