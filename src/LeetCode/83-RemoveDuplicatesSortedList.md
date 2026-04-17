# Bài toán Remove Duplicates from Sorted List
## Đề Bài
- Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
```
Input: head = [1,1,2]
Output: [1,2]
```
Example 2:
```
Input: head = [1,1,2,3,3]
Output: [1,2,3]
```

## Giải thích thuật toán bài toán Remove Duplicates from Sorted List
- Thuật toán dựa trên đặc điểm danh sách liên kết đã được **sắp xếp tăng dần**.
- Vì đã sắp xếp, các giá trị giống nhau sẽ nằm **liền kề** nhau (ví dụ: `1 → 1 → 2`).
- Thay vì tạo danh sách mới để lọc, ta tận dụng chính danh sách cũ và thay đổi **mối liên kết `next`** giữa các `ListNode`.
- Khi phát hiện node hiện tại và node kế tiếp có giá trị bằng nhau, ta "bắc cầu" bỏ qua node kế tiếp đó, liên kết thẳng tới node phía sau nó (`current.next = current.next.next`).
- Quá trình này giúp loại bỏ bản sao mà **không cần cấp phát thêm bộ nhớ** ngoài một vài biến con trỏ.

### Cách tiếp cận: 
- Sử dụng kỹ thuật **con trỏ kép (two pointers)** nhưng chỉ cần **một con trỏ duy nhất** do danh sách đã được sắp xếp.
- Tận dụng tính chất: **các phần tử trùng lặp luôn đứng liền kề nhau**.
- Duyệt qua danh sách, nếu giá trị node hiện tại bằng giá trị node kế tiếp, ta **bỏ qua node kế tiếp** bằng cách chỉnh lại liên kết `.next`.
- **Không tạo thêm mảng hay danh sách mới** – thao tác trực tiếp trên cấu trúc `ListNode` gốc (in-place).

### Tóm tắt các bước thực hiện
- **Bước 1:** Gán con trỏ `current = head` để bắt đầu duyệt từ đầu danh sách.
- **Bước 2:** Lặp qua danh sách với điều kiện `current` và `current.next` đều không rỗng (`None`).
- **Bước 3:** Tại mỗi bước lặp:
    - So sánh `current.val` và `current.next.val`.
    - **Nếu bằng nhau (trùng lặp):**
        - Thực hiện `current.next = current.next.next` để bỏ qua node trùng lặp.
        - **Không di chuyển `current`** vì node mới trỏ đến có thể vẫn trùng với `current`.
    - **Nếu khác nhau:**
        - Di chuyển `current` sang node kế tiếp: `current = current.next`.
- **Bước 4:** Kết thúc vòng lặp, trả về `head` (node đầu tiên của danh sách đã được loại bỏ trùng lặp).

## Độ phức tạp của thuật toán
- Time Complexity: `O(n)` với `n` là số lượng node trong danh sách liên kết.
- Space Complexity: `O(1)` (không gian hằng số).