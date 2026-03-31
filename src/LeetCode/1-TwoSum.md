# Bài toán TwoSum

## Đề Bài
- Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
- Example 1:

```markdown
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

- Example 2:

```markdown
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

- Example 3:

```markdown
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Giải thích thuật toán bài toán TwoSum
- Yêu cầu cốt lõi là tìm hai số a và b trong mảng sao cho:
```
a + b = target
```
- Điều này tương đương với việc: Nếu bạn đang đứng trước một số a, thì số b bạn cần tìm sẽ bằng target - a.

### Cách tiếp cận đầu tiên: Vét cạn (Brute Force)
**Hãy tưởng tượng bạn làm việc này bằng tay. Bạn sẽ làm thế nào?**
- Bạn lấy số đầu tiên.
- Bạn cộng nó với tất cả các số còn lại xem có bằng `target` không.
- Nếu không, bạn lấy số thứ hai và lặp lại quy trình.
**Hãy thử tư duy về độ phức tạp:**
- Nếu mảng có `n` phần tử. Với mỗi phần tử, bạn phải duyệt qua bao nhiêu phần tử còn lại?
- Tổng số bước thực hiện khoảng $n \times n$.
- Cách này dễ viết nhưng nếu mảng có 10.000 số thì chương trình sẽ chạy rất chậm.

### Cách tiếp cận tối ưu: Sử dụng Bảng tra cứu (Hash Map)
**Tư duy như sau:**
- Giả sử bạn đi dọc theo mảng từ trái sang phải.
1. Tại vị trí hiện tại, bạn có số `num`. Bạn cần tìm một người bạn `complement` sao cho `num + complement = target`. Tức là `complement = target - num`.
2. Bạn tự hỏi: *"Liệu số `complement` này có xuất hiện ở đằng trước (bên trái) mình không?"*
3. Nếu câu trả lời là **CÓ**, bạn đã tìm ra đáp án (vì bạn đang giữ số hiện tại và biết vị trí số cũ).
4. Nếu câu trả lời là **KHÔNG**, bạn ghi nhận số hiện tại này vào một cuốn sổ (bảng tra cứu) để các số phía sau có thể nhìn thấy nó.
**Cấu trúc dữ liệu:**
Để tra cứu xem một số đã xuất hiện chưa một cách nhanh nhất (tức thì), chúng ta sử dụng **Hash Map** (hoặc Dictionary/unordered_map tùy ngôn ngữ).
- **Key (Khóa):** Là giá trị của số (`value`).
- **Value (Giá trị):** Là chỉ số của số đó trong mảng (`index`).

## Độ phức tạp của thuật toán
- Time Complexity: O(n)