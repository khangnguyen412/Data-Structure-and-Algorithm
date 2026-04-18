# Bài toán Merge Sorted Array
## Đề Bài
- You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
- Merge nums1 and nums2 into a single array sorted in non-decreasing order.
- The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

- Example 1:
```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```
Example 2:
```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and []. The result of the merge is [1].
```
Example 3:
```
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1]. Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
```

## Giải thích thuật toán bài toán Merge Sorted Array
- Đây là bài toán **trộn hai mảng đã sắp xếp** thành một mảng duy nhất vẫn giữ thứ tự tăng dần.
- **Điểm đặc biệt:** Mảng đích `nums1` đã được cấp phát sẵn **vùng đệm** gồm `n` phần tử `0` ở cuối, đủ chỗ cho toàn bộ phần tử của `nums2`.
- Thuật toán áp dụng **kỹ thuật hai con trỏ chạy ngược từ cuối mảng**:
  - Một con trỏ `p1` đặt tại phần tử có nghĩa cuối cùng của `nums1` (vị trí `m-1`).
  - Một con trỏ `p2` đặt tại phần tử cuối cùng của `nums2` (vị trí `n-1`).
  - Một con trỏ `p` đặt tại vị trí cuối cùng của mảng kết quả `nums1` (vị trí `m+n-1`).
- **Nguyên lý hoạt động:**
  - Tại mỗi bước, so sánh `nums1[p1]` và `nums2[p2]`.
  - **Đưa phần tử lớn hơn vào `nums1[p]`**, sau đó lùi con trỏ tương ứng (`p1` hoặc `p2`) và lùi `p`.
  - Lặp lại cho đến khi một trong hai mảng nguồn được duyệt hết.
  - Nếu `nums2` vẫn còn phần tử, chép nốt chúng vào vị trí đầu của `nums1` (vì các vị trí đó đã được "giải phóng").
  - Nếu `nums1` hết trước thì không cần làm gì thêm, vì các phần tử còn lại của `nums1` đã nằm sẵn đúng vị trí đầu mảng.
- **Ưu điểm:**
  - **Không cần dịch chuyển phần tử** nào trong `nums1` do ta điền từ phải sang trái, tận dụng chính xác các ô trống `0`.
  - **Không dùng thêm mảng phụ**, bộ nhớ O(1).
  - Thời gian tuyến tính O(m + n).

### Cách tiếp cận: 
- **Dùng ba con trỏ ảo** để theo dõi vị trí hiện tại của các phần tử trong `nums1` (phần có nghĩa) và `nums2`, và vị trí đích trong `nums1`.
- **Điền từ cuối mảng `nums1` trở về đầu** để tận dụng các ô trống (`0`) có sẵn, tránh phải dịch chuyển phần tử.
- **So sánh hai phần tử lớn nhất chưa được xử lý** từ `nums1` và `nums2`, đặt phần tử lớn hơn vào vị trí đích hiện tại.
- **Xử lý riêng các trường hợp biên**:
  - Khi `nums2` đã hết phần tử: không cần làm gì thêm vì `nums1` đã chứa sẵn các phần tử còn lại ở đúng vị trí.
  - Khi `nums1` không có phần tử hợp lệ (`m == 0`): chỉ cần chép trực tiếp các phần tử còn lại từ `nums2`.
- Vòng lặp chỉ chạy đúng số lần cần thiết (tối đa `m + n` lần) và dừng sớm khi `nums2` rỗng.

### Tóm tắt các bước thực hiện
- **Bước 1:** Khởi tạo vòng lặp `for i in range(m + n - 1, -1, -1)` để duyệt ngược từ vị trí cuối cùng của mảng kết quả về đầu.
- **Bước 2:** Nếu `n == 0` (toàn bộ `nums2` đã được chép), dùng `break` thoát vòng lặp vì không còn việc gì để làm.
- **Bước 3:** Nếu `m == 0` (không còn phần tử hợp lệ nào trong `nums1`), thực hiện:
  - Gán `nums1[i] = nums2[n - 1]` (lấy phần tử cuối cùng hiện tại của `nums2`).
  - Giảm `n` đi 1.
  - `continue` để bỏ qua phần so sánh bên dưới và chuyển sang vòng lặp tiếp theo.
- **Bước 4:** So sánh phần tử cuối cùng có nghĩa của `nums1` (`nums1[m - 1]`) với phần tử cuối cùng của `nums2` (`nums2[n - 1]`):
  - Nếu `nums1[m - 1] > nums2[n - 1]`:
    - Đặt `nums1[i] = nums1[m - 1]`.
    - Giảm `m` đi 1 (đã dùng một phần tử của `nums1`).
  - Ngược lại:
    - Đặt `nums1[i] = nums2[n - 1]`.
    - Giảm `n` đi 1 (đã dùng một phần tử của `nums2`).
- **Bước 5:** Lặp lại các bước 2–4 cho đến khi vòng lặp kết thúc.
- **Kết quả:** Sau khi vòng lặp kết thúc, `nums1` đã chứa toàn bộ `m + n` phần tử được sắp xếp tăng dần.

## Độ phức tạp của thuật toán
- Time Complexity: `O(m + n)`  
  - Mỗi phần tử của `nums1` (phần có nghĩa) và `nums2` được xử lý **tối đa một lần**.
  - Vòng lặp chạy tối đa `m + n` bước, mỗi bước thực hiện thao tác hằng số.
- Space Complexity: `O(1)`  
  - Thuật toán **không sử dụng thêm bộ nhớ phụ trợ** (không tạo mảng mới, chỉ thao tác trực tiếp trên `nums1` và một vài biến đếm).