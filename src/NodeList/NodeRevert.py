class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head: ListNode | None = None

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

    def revert_list_node(self):
        prev, cur = None, self.head
        while cur:
            next = cur.next  # Tạo nối tạm (để sau khi đảo node, cur ko bị mất cur.next)
            cur.next = prev  # Thao tác đảo (cur.next trỏ về prev)
            prev = cur  # Node hiện tại thành node trước
            cur = next  # Chuyển sang node kế tiếp đẽ xử lý
        return prev


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]

    sol.head = sol.convert_to_node(nums)
    print(f"Danh sách ban đầu: {sol.convert_from_node()}")
    
    sol.head = sol.revert_list_node()
    print(f"Danh sách sau đảo ngược: {sol.convert_from_node()}")
