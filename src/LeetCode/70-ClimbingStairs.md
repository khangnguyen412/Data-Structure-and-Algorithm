# Bài toán Climbing Stairs
## Đề Bài
- You are climbing a staircase. It takes n steps to reach the top.
- Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```
Example 2:
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

## Giải thích thuật toán bài toán Climbing Stairs
- Cho một cầu thang có `n` bậc.
- Mỗi bước, bạn chỉ được leo **1 bậc** hoặc **2 bậc**.
- Hỏi: có bao nhiêu **cách khác nhau** để leo từ mặt đất lên tới bậc thứ `n`?
- Thứ tự các bước quan trọng (ví dụ: 1+2 khác 2+1).

### Cách tiếp cận: 
- Nhận xét: Để lên được bậc `i`, bạn chỉ có thể đến từ bậc `i-1` (bước 1 bậc) hoặc bậc `i-2` (bước 2 bậc).
- Gọi `dp[i]` là số cách leo lên bậc `i`.
- Công thức truy hồi:  
  `dp[i] = dp[i-1] + dp[i-2]`
- Cơ sở:  
  `dp[0] = 1` (đứng tại mặt đất – không bước nào)  
  `dp[1] = 1` (chỉ có 1 cách: bước 1 bậc)
- Từ `dp[0]` và `dp[1]`, ta tính tuần tự `dp[2]`, `dp[3]`, …, `dp[n]` bằng vòng lặp.
- Kết quả cần tìm là `dp[n]`.

### Tóm tắt các bước thực hiện
1. Khởi tạo hai biến `a = 1` (ứng với `dp[0]`) và `b = 1` (ứng với `dp[1]`).
2. Nếu `n <= 1`, trả về `1`.
3. Dùng vòng lặp `for i` từ `2` đến `n`:
   - Tính `c = a + b`
   - Gán `a = b`, `b = c`
4. Kết thúc vòng lặp, `b` chính là `dp[n]` – số cách leo lên bậc `n`.

## Độ phức tạp của thuật toán
- Time Complexity: `O(n)` – chỉ có một vòng lặp chạy `n-1` lần.
- Space Complexity: `O(1)` – chỉ dùng 3 biến số, không dùng mảng phụ.