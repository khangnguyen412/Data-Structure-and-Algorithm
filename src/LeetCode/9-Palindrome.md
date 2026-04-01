# Bài toán Palindrome Number

## Đề Bài
- Given an integer x, return true if x is a palindrome, and false otherwise.

- Example 1:
```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

- Example 2:
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

- Example 3:
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

## Giải thích thuật toán bài toán Palindrome Number
- Trước khi làm tính toán phức tạp, hãy tự hỏi: Có số nào nhìn vào là biết ngay không phải palindrome không?
    - Số âm: Số âm có thể là palindrome không? Ví dụ: -121. Đọc ngược là 121-. Nó khác với ban đầu. Vậy kết luận ngay về số âm là gì?
    - Số kết thúc bằng 0: Ví dụ số 10. Đọc ngược sẽ là 01 (tức là 1). Nó không bằng 10. Vậy một số kết thúc bằng số 0 (trừ chính số 0) có thể là palindrome không?

### Cách tiếp cận 1: Chuyển sang chuỗi (String)
*   Ý tưởng: Bạn chuyển số nguyên `x` thành một chuỗi ký tự.
*   Sau đó, bạn so sánh chuỗi đó với phiên bản đảo ngược của chính nó.
*   *Ưu điểm:* Rất dễ viết code (thường chỉ cần 1 dòng).
*   *Nhược điểm:* Tốn thêm bộ nhớ để tạo chuỗi.

### Cách tiếp cận 2: Toán học (Mathematical Approach) - Khuyên dùng
*   Ý tưởng: Chúng ta sẽ đảo ngược số đó bằng toán học và so sánh với số gốc.
*   **Câu hỏi quan trọng:** Bạn sẽ làm thế nào để lấy được chữ số cuối cùng của một số nguyên? (Gợi ý: Phép chia lấy dư `%`).
*   **Câu hỏi tiếp theo:** Sau khi lấy được chữ số cuối, làm thế nào để bỏ nó đi để lấy số kế tiếp? (Gợi ý: Phép chia nguyên `/`).
*   **Ví dụ minh họa:**
    *   Số: `123`
    *   Lấy số cuối: `123 % 10 = 3`.
    *   Bỏ số cuối đi: `123 / 10 = 12`.

### Tối ưu hóa (Tư duy nửa số)
Nếu đảo ngược toàn bộ con số, có nguy cơ bị tràn số (overflow) nếu con số quá lớn (ví dụ số lớn hơn 2 tỷ).
*   **Gợi ý:** Bạn có thực sự cần đảo ngược toàn bộ số không?
*   Hãy tưởng tượng số `12321`.
    *   Nếu ta chỉ đảo ngược một nửa số, ta sẽ được `123` (số gốc bị cắt) và `12` (số đảo ngược).
    *   Vì số lẻ có chữ số ở giữa (số 3), ta có thể bỏ qua chữ số đó bằng phép chia cho 10.
    *   Điều kiện dừng vòng lặp là gì? Khi số đảo ngược bắt đầu lớn hơn hoặc bằng số gốc còn lại.

## Độ phức tạp của thuật toán
- Time Complexity: O(n)