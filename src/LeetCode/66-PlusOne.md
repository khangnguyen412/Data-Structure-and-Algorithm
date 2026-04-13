# Bài toán Plus One
## Đề Bài
- You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
- Increment the large integer by one and return the resulting array of digits.

Example 1:
```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```
Example 2:
```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```
Example 3:
```
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```

## Giải thích thuật toán bài toán Plus One
- Bài toán yêu cầu cộng thêm 1 vào số nguyên lớn được biểu diễn dưới dạng mảng các chữ số. Thay vì chuyển thành số nguyên (dễ bị tràn khi mảng dài), ta mô phỏng phép cộng từ hàng đơn vị (cuối mảng) lên hàng cao nhất, xử lý nhớ giống như phép cộng tay.

### Cách tiếp cận: 
- Duyệt mảng từ phải sang trái (từ chữ số hàng đơn vị lên hàng cao nhất).
   - Nếu gặp chữ số nhỏ hơn 9, chỉ cần tăng nó lên 1 và kết thúc (vì không có nhớ tiếp).
   - Nếu gặp chữ số 9, đặt nó thành 0 (vì 9+1=10, viết 0 nhớ 1) và tiếp tục duyệt sang trái để xử lý nhớ.
   - Nếu duyệt hết mảng mà vẫn còn nhớ (tức tất cả các chữ số đều là 9), ta thêm chữ số 1 vào đầu mảng.

### Tóm tắt các bước thực hiện
- Duyệt `i` từ `len(digits) - 1` xuống `0`.  
- Nếu `digits[i] < 9`:  
   - Tăng `digits[i]` lên 1.  
   - Trả về `digits` (kết thúc).  
- Nếu `digits[i] == 9`:  
   - Gán `digits[i] = 0`.  
   - Tiếp tục vòng lặp (xử lý nhớ).  
- Sau vòng lặp (nếu chưa trả về), tức tất cả các phần tử đều là 9 → trả về `[1] + digits`.

## Độ phức tạp của thuật toán
- Time Complexity: O(n)
- Space Complexity: O(1)