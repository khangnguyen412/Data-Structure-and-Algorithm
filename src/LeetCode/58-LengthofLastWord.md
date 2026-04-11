# Bài toán Length of Last Word
## Đề Bài
- Given a string s consisting of words and spaces, return the length of the last word in the string.
- A word is a maximal substring consisting of non-space characters only.

Example 1:
```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```
Example 2:
```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```
Example 3:
```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
``` 
Example 4:
```
Input: s = "a"
Output: 1
```

## Giải thích thuật toán bài toán Length of Last Word
- Bài toán yêu cầu tìm độ dài của từ cuối cùng trong một chuỗi có thể chứa nhiều khoảng trắng ở đầu, giữa và cuối. 

### Cách tiếp cận: 
- Tận dụng `strip()` để đơn giản hóa bài toán, loại bỏ các khoảng trắng dư thừa ở hai đầu, đảm bảo rằng ký tự cuối cùng của chuỗi sau khi strip là ký tự cuối của từ cuối. 
- Sau đó, chỉ cần đếm số lượng ký tự liên tiếp từ cuối lên cho đến khi gặp khoảng trắng hoặc hết chuỗi.

### Tóm tắt các bước thực hiện
1. Loại bỏ khoảng trắng đầu và cuối chuỗi `s` bằng `s.strip()` lưu vào `trim_s`.
2. Khởi tạo biến `length_of_last_word = 0`.
3. Duyệt `i` từ chỉ số cuối của `trim_s` về `0` (giảm dần 1):
   - Nếu `trim_s[i]` là khoảng trắng: trả về `length_of_last_word` ngay lập tức.
   - Ngược lại, tăng `length_of_last_word` lên 1.
4. Nếu vòng lặp kết thúc (chuỗi chỉ có một từ), trả về `length_of_last_word`.

## Độ phức tạp của thuật toán
- Time Complexity: 
- Space Complexity: 
