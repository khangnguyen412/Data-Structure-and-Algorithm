class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head: ListNode | None = None

    def convert_to_node(self, arr):
        if arr is None:
            return
        if not arr:
            return None
        dummy = ListNode(0)
        cur = dummy
        for val in arr:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next

    def find_node(self, target=int):
        cur = self.head
        while cur:
            if cur.val == target:
                return cur.val
            cur = cur.next


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3]

    sol.head = sol.convert_to_node(arr)    
    print(f"Giá trị được tìm thấy tại: {sol.find_node(2)}")
