# Node : Khái niệm & Khai báo (Cheat Sheet)

## 1. Node là gì?
| Thuộc tính | Ý nghĩa |
|------------|---------|
| **Định nghĩa** | Đơn vị dữ liệu nhỏ nhất trong cấu trúc liên kết (Linked List, Tree, Graph). |
| **Cấu trúc** | Gồm 2 phần: `value` (dữ liệu) + `pointer/reference` (trỏ đến node khác). |
| **Đặc điểm Python** | Không dùng con trỏ (pointer) như C/C++. Python dùng **object reference** → biến chứa địa chỉ vùng nhớ của object. |
| **Điểm kết thúc** | `None` đánh dấu node cuối (không trỏ đi đâu nữa). |

> **Hình dung trong đầu:**  
> `Node(3, next) → [val: 3 | ref: ───▶] ───▶ [val: 7 | ref: ───▶ None]`

---

## 2. Khai báo Node chuẩn

### Singly Linked List
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Tree List
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```