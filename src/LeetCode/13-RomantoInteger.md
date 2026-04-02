# Bài toán Roman to Integer

## Đề Bài
- Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
```
| Symbol    | Value |
| ---       | ---   |
| I         | 1     |
| V         | 5     |
| X         | 10    |
| L         | 50    |
| C         | 100   |
| D         | 500   |
| M         | 1000  |
```

- For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
- Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
    - I can be placed before V (5) and X (10) to make 4 and 9.
    - X can be placed before L (50) and C (100) to make 40 and 90.
    - C can be placed before D (500) and M (1000) to make 400 and 900.
- Given a roman numeral, convert it to an integer.

- Example:
```
Input: s = "III"
Output: 3
Explanation: III = 3.
```

```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

- `1 <= s.length <= 15`
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

## Giải thích thuật toán bài toán Roman to Integer
- Nếu chỉ "cộng dồn tiếp cho giá trị trước" theo thứ tự từ trái sang phải, bạn sẽ gặp lỗi ở các số đặc biệt (như IV, IX, CM...).
- Ví dụ: Số **IV** (4).
    - Nếu theo tư duy cộng dồn thông thường: I (1) + V (5) = 6 -> **Sai**.
    - Đúng phải là: 5 - 1 = 4.
- Để giải quyết đúng, bạn cần điều chỉnh tư duy một chút như sau:

### 1. Tư duy cốt lõi: So sánh "Hiện tại" với "Tiếp theo"
- Thay vì chỉ cộng dồn, bạn hãy nghĩ theo quy tắc: **"Nhìn trước để quyết định hành động"**.
- Khi đang đứng ở một ký tự bất kỳ trong chuỗi Roman:
    - Hãy nhìn sang ký tự **bên phải** (ký tự tiếp theo).
    - So sánh giá trị của **Ký tự hiện tại** với **Ký tự tiếp theo**.
- Có 2 trường hợp xảy ra:
    - **Trường hợp 1: Giá trị hiện tại NHỎ HƠN giá trị tiếp theo** (Ví dụ: I đứng trước V).
        - Điều này báo hiệu phép trừ (nguyên tắc IV = 4, IX = 9).
        - **Hành động:** Lấy kết quả tổng hiện tại trừ đi giá trị hiện tại.
    - **Trường hợp 2: Giá trị hiện tại LỚN HƠN HOẶC BẰNG giá trị tiếp theo** (Ví dụ: V đứng trước I trong VI, hoặc X đứng trước X trong XX).
        - Đây là phép cộng thông thường.
        - **Hành động:** Lấy kết quả tổng hiện tại cộng thêm giá trị hiện tại.

### Cách tiếp cận: 
- Bạn có thể hình dung các bước lập trình như sau:
    1. **Khởi tạo:** Một biến `total = 0` để lưu kết quả, và một bảng tra cứu giá trị (Map hoặc Switch case) cho các ký tự I, V, X, L, C, D, M.
    2. **Duyệt chuỗi:** Chạy một vòng lặp từ đầu đến cuối chuỗi (hoặc đến sát cuối).
    3. **Tại mỗi vị trí `i`:**
        - Lấy giá trị ký tự hiện tại gọi là `curr`.
        - Lấy giá trị ký tự tiếp theo gọi là `next` (nếu có, nếu không có thì coi như 0).
        - **So sánh:**
            - Nếu `curr < next`: `total = total - curr` (Trừ đi).
            - Ngược lại: `total = total + curr` (Cộng vào).
    4. **Kết thúc:** Trả về `total`.

## Độ phức tạp của thuật toán
- Time Complexity: O(n)