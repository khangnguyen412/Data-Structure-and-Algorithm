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

    def remove_from_position(self, val):
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


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 4, 3]

    sol.head = sol.convert_to_node(nums)
    print(f"Danh sách ban đầu: {sol.convert_from_node()}")

    sol.remove_from_position(4)
    print(f"Danh sách sau khi xoá node 4: {sol.convert_from_node()}")
