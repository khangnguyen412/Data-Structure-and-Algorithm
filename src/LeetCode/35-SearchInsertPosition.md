# Bài toán Search Insert Position

## Đề Bài
- Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
- You must write an algorithm with O(log n) runtime complexity.
Example 1:
```
Input: nums = [1,3,5,6], target = 5
Output: 2
```
Example 2:
```
Input: nums = [1,3,5,6], target = 2
Output: 1
```
Example 3:
```
Input: nums = [1,3,5,6], target = 7
Output: 4
```
## Giải thích thuật toán bài toán Search Insert Position
- Vì mảng đã được sắp xếp tăng dần, nếu ta duyệt từ đầu đến cuối, phần tử đầu tiên lớn hơn hoặc bằng target sẽ quyết định vị trí cần tìm:
    - Nếu phần tử đó bằng target → đó chính là index cần trả về.
    - Nếu phần tử đó lớn hơn target → target chưa có trong mảng, và vị trí hiện tại là nơi target nên được chèn vào để giữ thứ tự.
- Nếu ta duyệt hết mảng mà vẫn không gặp phần tử nào >= target, điều đó có nghĩa là target lớn hơn tất cả các phần tử → vị trí chèn là cuối mảng (index = len(nums)).

### Cách tiếp cận: 
- Duyệt tuyến tính (linear scan) từ đầu đến cuối mảng.
- Vì mảng đã được sắp xếp tăng dần, phần tử đầu tiên thỏa mãn nums[i] >= target chính là vị trí cần trả về (hoặc vị trí chèn).
- Nếu duyệt hết mà không gặp phần tử nào như vậy, target lớn hơn tất cả → vị trí chèn là cuối mảng (bằng độ dài mảng).

### Tóm tắt các bước thực hiện
- Khởi tạo vòng lặp for i in range(len(nums)).
- Với mỗi i, kiểm tra nếu nums[i] >= target:
    - Nếu đúng → trả về i (vì tìm thấy target hoặc tìm đúng vị trí cần chèn).
- Sau vòng lặp (không tìm thấy phần tử nào >= target) → trả về len(nums).

## Độ phức tạp của thuật toán
- Time Complexity:  O(n) – phải duyệt tối đa toàn bộ mảng trong trường hợp target lớn hơn mọi phần tử.
- Space Complexity: O(1) – chỉ dùng biến chỉ số vòng lặp, không cấp phát thêm bộ nhớ phụ thuộc vào đầu vào.
