# Bài toán Longest Common Prefix

## Đề Bài
- Write a function to find the longest common prefix string amongst an array of strings.
- If there is no common prefix, return an empty string `""`.

- **Example 1:**
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

- **Example 2:**
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

- **Constraints:**
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters if it is non-empty.

## Giải thích thuật toán bài toán Longest Common Prefix
- **Prefix (Tiền tố):** Trong tiếng Anh, "Prefix" nghĩa là tiền tố, tức là **các ký tự đầu tiên** của một từ. Ví dụ: Từ "Hello", tiền tố dài 1 ký tự là "H", tiền tố dài 2 ký tự là "He", tiền tố dài 3 ký tự là "Hel".
- **Common (Chung):** Các ký tự đầu tiên này phải giống hệt nhau ở **tất cả** các chuỗi trong mảng.
- **Tóm lại:** Bài toán yêu cầu tìm một đoạn ký tự đầu tiên mà tất cả các từ trong mảng đều có chung.

### Cách tiếp cận: 
- Cách giải quyết đơn giản và trực quan nhất là **"So sánh theo chiều dọc" (Vertical Scanning)**.
- **Tư duy:**
    1. Bạn lấy ký tự đầu tiên của từ đầu tiên (ví dụ chữ 'f' trong "flower").
    2. Bạn đi kiểm tra xem từ thứ 2 ("flow") và từ thứ 3 ("flight") có chữ 'f' ở vị trí đầu tiên không?
        - Nếu có $\rightarrow$ tiếp tục xét ký tự thứ 2.
        - Nếu không $\rightarrow$ Dừng lại và trả về kết quả đã tìm được trước đó.
    3. Lặp lại quy trình cho các vị trí tiếp theo (index 1, index 2...).
- **Giả mã (Pseudo code):**
    1. Nếu mảng rỗng, trả về `""`.
    2. Lấy từ đầu tiên làm chuẩn (gọi là `firstStr`).
    3. Duyệt qua từng ký tự của `firstStr` (với chỉ số `i`):
        - Duyệt qua các từ còn lại trong mảng (gọi là `s`):
            - Nếu như độ dài của từ `s` ngắn hơn `i` (hết từ) HOẶC ký tự tại `s[i]` khác với `firstStr[i]`:
                - Trả về `firstStr` cắt từ 0 đến `i` (tức là phần prefix đã khớp).
    4. Nếu duyệt hết mà không có gì sai khác, trả về luôn `firstStr` (trường hợp từ đầu tiên ngắn nhất và là tiền tố của tất cả các từ còn lại).

## Độ phức tạp của thuật toán
- Time Complexity: O(m × n). 
  - m: là độ dài chuỗi ngắn nhất trong strs.
  - n: là số chuỗi trong strs.
- Space Complexity: O(1).