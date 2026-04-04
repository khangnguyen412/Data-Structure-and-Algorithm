# Bài toán Valid Parentheses

## Đề Bài
- Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
- An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

- Example 1:
```
Input: s = "()"
Output: true
```

- Example 2:
```
Input: s = "()[]{}"
Output: true
```

- Example 3:
```
Input: s = "(]"
Output: false
```

- Example 4:
```
Input: s = "([])"
Output: true
```

- Example 5:
```
Input: s = "([)]"
Output: false
```

## Giải thích thuật toán bài toán Valid Parentheses
Hãy nhìn vào các ví dụ bạn đã đưa ra, đặc biệt là ví dụ số 4 `([])` và ví dụ số 5 `([)]`.

**Ví dụ 4:** `([])` -> Hợp lệ.
    - Dấu `(` mở ra, rồi dấu `[` mở ra.
    - Dấu `]` đóng lại dấu `[`.
    - Dấu `)` đóng lại dấu `(`.
    - **Quan sát:** Dấu ngoặc mở **sau cùng** phải được đóng **đầu tiên**.

**Ví dụ 5:** `([)]` -> Không hợp lệ.
    - Dấu `(` mở ra, rồi dấu `[` mở ra.
    - Dấu `)` xuất hiện cố gắng đóng dấu `(`, nhưng dấu `[` bên trong vẫn chưa được đóng.
    - **Quan sát:** Sự xâm lấn lẫn nhau (giao thoa) là không được phép.

**Kết luận quan trọng:**
    - Bài toán này tuân theo nguyên tắc **LIFO** (Last In, First Out) - *Vào sau, Ra trước*.
    - Dấu ngoặc nào mở ra sau cùng thì phải là dấu ngoặc được đóng đầu tiên. Tư duy này dẫn thẳng đến một cấu trúc dữ liệu cụ thể.

### Cách tiếp cận: 
- Giả sử chúng ta có một Stack rỗng. Chúng ta sẽ duyệt qua từng ký tự trong chuỗi `s`:

**Trường hợp 1: Gặp dấu MỞ NGOẶC (`(`, `{`, `[`)**
- Chúng ta chưa thể kết luận ngay nó có hợp lệ hay không vì chưa thấy dấu đóng.
- **Hành động:** Đẩy (Push) ký tự này vào Stack để "nhớ" rằng đang có một dấu ngoặc mở chờ được đóng.

**Trường hợp 2: Gặp dấu ĐÓNG NGOẶC (`)`, `}`, `]`)**
- Lúc này, chúng ta cần kiểm tra xem nó có khớp với dấu mở gần nhất hay không.
- **Hành động:** Lấy (Pop) phần tử trên cùng của Stack ra.
    - Nếu Stack rỗng (không có gì để lấy ra) -> Sai quy tắc (thừa dấu đóng) -> **False**.
    - Nếu lấy ra được, nhưng ký tự lấy ra không khớp với dấu đóng hiện tại (ví dụ: đang mở `(` mà đóng là `]`) -> Sai loại -> **False**.
    - Nếu lấy ra và khớp đúng cặp -> Tiếp tục xét ký tự tiếp theo.

**Trường hợp 3: Duyệt xong toàn bộ chuỗi**
- Sau khi duyệt hết chuỗi, nếu Stack vẫn còn phần tử (tức là còn dấu mở ngoặc mà chưa ai đóng) -> Thiếu dấu đóng -> **False**.
- Nếu Stack rỗng hoàn toàn -> Tất cả đã khớp đôi -> **True**.

### Các trường hợp "biên" (Edge Cases) cần lưu ý

Khi viết code, bạn cần đặc biệt cẩn thận các trường hợp sau để tránh lỗi runtime hoặc logic:

1. **Chuỗi lẻ (Odd length):** Nếu chuỗi có độ dài lẻ (ví dụ: `(()`), chắc chắn sẽ không hợp lệ vì mỗi cặp cần 2 phần tử. Đây là điều kiện kiểm tra nhanh để tối ưu.
2. **Stack rỗng khi gặp dấu đóng:** Ví dụ chuỗi bắt đầu bằng `)`. Khi bạn thử `Pop` từ Stack, nếu Stack rỗng, chương trình sẽ bị lỗi nếu bạn không kiểm tra điều kiện `isEmpty` trước.
3. **Cặp ký tự không khớp:** Ví dụ `(]`. Stack có `(`, gặp `]` thì pop `(` ra, so sánh thấy không đúng cặp.

### Tóm tắt các bước thực hiện

Để giải quyết bài toán này, bạn cần chuẩn bị:
1. Một **Stack** rỗng.
2. Một bảng **Map** (ánh xạ) để định nghĩa cặp đôi: `)` đi với `(`, `]` đi với `[`, `}` đi với `{`. Điều này giúp code gọn gàng thay vì dùng quá nhiều câu lệnh `if-else`.

**Quy trình:**
- Duyệt chuỗi.
- Nếu là mở -> Push vào Stack.
- Nếu là đóng -> Pop ra và kiểm tra khớp không. Không khớp -> False.
- Hết chuỗi -> Kiểm tra Stack có rỗng không.

## Độ phức tạp của thuật toán
- Time Complexity: O(n)
- Space Complexity: O(n)
