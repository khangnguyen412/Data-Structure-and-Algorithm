# Bài toán Binary Tree Inorder Traversal
## Đề Bài
Given the root of a binary tree, return the inorder traversal of its nodes' values.
- Example 1:
```
Input: root = [1,null,2,3]
Output: [1,3,2]
Explanation:
1
 \
  2
 /
3
```
- Example 2:
```
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]
Explanation:
        1
       / \
      2   3
     / \   \
    4   5   8
       / \  /
      6   7 9
```
- Example 3:
```
Input: root = []
Output: []
```
- Example 4:
```
Input: root = [1]
Output: [1]
```
## Giải thích thuật toán bài toán Binary Tree Inorder Traversal
- Thuật toán **Inorder Traversal** duyệt cây nhị phân theo quy tắc: **Thăm cây con bên trái → Thăm nút hiện tại → Thăm cây con bên phải**. 
- Đây là một dạng duyệt DFS (Depth-First Search). Bạn có thể hình dung nó như "đi sâu vào bên trái cùng trước, rồi lùi lại để lấy giá trị, sau đó mới rẽ sang phải".

### Cách tiếp cận: 
Có **hai cách tiếp cận** cơ bản để giải bài toán này:
1. **Đệ quy (Recursive):** Rất ngắn gọn và dễ đọc. Hàm sẽ gọi chính nó cho node con trái, thêm giá trị node hiện tại vào kết quả, rồi gọi chính nó cho node con phải.
2. **Lặp với Ngăn xếp (Iterative with Stack):** Dùng một cái `stack` để mô phỏng hành vi của đệ quy. Cách này giúp bạn kiểm soát bộ nhớ rõ hơn và tránh lỗi "Recursion Limit" nếu cây quá sâu.


### Tóm tắt các bước thực hiện
**Cách 1: Đệ quy**
1. Nếu node hiện tại là `null` (None): Trả về một mảng rỗng `[]`.
2. Đệ quy gọi hàm cho node bên trái (`node.left`), lưu kết quả vào `left_vals`.
3. Tạo một mảng chứa giá trị của node hiện tại (`[node.val]`).
4. Đệ quy gọi hàm cho node bên phải (`node.right`), lưu kết quả vào `right_vals`.
5. Trả về kết quả bằng cách nối: `left_vals + [node.val] + right_vals`.

**Cách 2: Lặp với Stack**
1. Khởi tạo một `stack` rỗng và một biến `cur_node = root`.
2. Trong khi `stack` không rỗng hoặc `cur_node` không `null`:
   - Dùng vòng lặp `while cur_node:`: Đẩy `cur_node` vào stack và gán `cur_node = cur_node.left` cho đến khi chạm nút `null` (đi sâu nhất về bên trái).
   - Lấy node trên cùng ra khỏi stack (`cur_node = stack.pop()`).
   - Thêm `cur_node.val` vào mảng kết quả.
   - Gán `cur_node = cur_node.right` để sang nhánh phải.
3. Trả về mảng kết quả.

## Độ phức tạp của thuật toán
- **Time Complexity:** **O(n)** với `n` là tổng số node trong cây. Vì thuật toán phải duyệt qua mỗi node đúng một lần.
- **Space Complexity:** 
  - Với **Cách Đệ quy**: Tệ nhất là **O(n)** (nếu cây chỉ có một nhánh dài, stack hệ thống đệ quy sẽ cao bằng n), trung bình là **O(log n)** (với cây cân bằng).
  - Với **Cách Lặp bằng Stack**: Tệ nhất là **O(n)** (trường hợp cây chỉ có một nhánh, stack sẽ chứa tất cả các node), trung bình là **O(log n)**.