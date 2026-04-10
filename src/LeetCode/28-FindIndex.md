# Bài toán Find the Index of the First Occurrence in a String
## Đề Bài
- Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. 

Example 1:
```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```
Example 2:
```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```

## Giải thích thuật toán bài toán Find the Index of the First Occurrence in a String
- Bài toán yêu cầu tìm vị trí xuất hiện đầu tiên của chuỗi needle trong chuỗi haystack. Nếu needle không xuất hiện, trả về -1. Ví dụ:
    - haystack = "sadbutsad", needle = "sad" → trả về 0 (vì "sad" bắt đầu ở index 0).
    - haystack = "leetcode", needle = "leeto" → trả về -1.
- Ràng buộc: độ dài mỗi chuỗi từ 1 đến 10^4, chỉ gồm chữ cái in thường

### Cách tiếp cận: 
**Duyệt trực tiếp (Brute Force):**
- Duyệt từng vị trí i trong haystack từ 0 đến len(haystack) - len(needle).
- Với mỗi i, so sánh từng ký tự của needle với haystack[i : i+len(needle)].
- Nếu tất cả khớp, trả về i. Kết thúc vòng lặp, trả về -1.

### Tóm tắt các bước thực hiện
- Phương pháp Brute Force cho bài toán này thường dùng 2 vòng lặp lồng nhau:
    - Vòng lặp ngoài (i): chạy từ 0 đến len(haystack) - len(needle). Đây là vị trí bắt đầu tiềm năng trong haystack.
    - Vòng lặp trong (j): chạy từ 0 đến len(needle) - 1, dùng để so sánh từng ký tự needle[j] với haystack[i + j].
- Nếu tất cả các ký tự đều khớp (vòng trong chạy hết mà không có sai khác), ta trả về i. Nếu vòng trong phát hiện ký tự khác, ta thoát sớm và tăng i lên 1 để thử vị trí tiếp theo.
## Độ phức tạp của thuật toán
- Time Complexity: O(n * m) trong trường hợp xấu nhất, khi haystack và needle có độ dài lớn và haystack chứa nhiều phần giống với needle.
- Space Complexity: O(1)
