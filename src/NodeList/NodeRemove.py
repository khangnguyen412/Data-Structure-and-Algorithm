class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head: ListNode = None

    def convert_to_node(self, arr=None):
        if arr is None:
            arr = []
        if not arr:
            return None
        dummy = ListNode(0)
        cur = dummy
        for val in arr:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next

    def convert_from_node(self):
        res, cur = [], self.head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

    def remove_head_node(self):
        if not self.head:
            return
        
        if not self.head.next:
            self.head = None
        else:
            self.head = self.head.next
            return

    def remove_with_value(self, val):
        prev = None
        found = False
        cur = self.head
        while cur:
            if cur.val == val:
                prev.next = cur.next  # cắt bỏ node hiện tại, nối prev với node tiếp theo
                found = True  # set đã tìm thấy node
                break
            prev = cur  # set node hiện tại thành node cũ trước khi nãy sang node
            cur = cur.next  # nhảy node
        if found == False:
            print(f"không thấy node có giá trị {val}")

    def remove_last_node(self):
        if not self.head: # nếu node rỗng
            return
        
        if not self.head.next: # nếu của có một node
            self.head = None
            return
        
        """
        Để xóa một node, bạn bắt buộc phải tác động vào node đứng trước nó để hủy liên kết.
        Nếu bạn dùng while cur.next: để đi tới node cuối cùng, bạn sẽ gặp hai vấn đề sau:
        
        1. Bản chất của việc gán None
            Khi vòng lặp dừng ở node cuối, biến cur đang đại diện cho chính node cuối đó.
            Nếu bạn viết cur = None, bạn chỉ làm cho biến tạm cur biến mất. Node cuối thực tế trong bộ nhớ vẫn còn liên kết với node kế cuối. Danh sách không hề thay đổi.
        
        2. Danh sách liên kết là đường 1 chiều
            Khi bạn đã đứng ở node cuối cùng, bạn không thể quay lại node kế cuối được nữa vì danh sách liên kết đơn chỉ đi về phía trước.
            Do không quay lại được, bạn không thể sửa lệnh next của node kế cuối thành None.        
        """
        cur = self.head
        while cur.next.next: # nếu có 2 node trở lên nhảy tới nói cuối
            cur = cur.next

        cur.next=None

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 4, 3, 4, 5, 6]

    sol.head = sol.convert_to_node(nums)
    print(f"Danh sách ban đầu: {sol.convert_from_node()}")

    sol.remove_with_value(4)
    print(f"Danh sách sau khi xoá node 4: {sol.convert_from_node()}")

    sol.remove_head_node()
    print(f"Danh sách sau khi xoá node đầu tiên: {sol.convert_from_node()}")

    sol.remove_last_node()
    print(f"Danh sách sau khi xoá node đầu cuối: {sol.convert_from_node()}")

