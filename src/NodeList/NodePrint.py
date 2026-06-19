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

    def print_list_node(self):
        cur = self.head
        while cur:
            print(f"Giá trị của node hiện tại: {cur.val}")
            cur = cur.next


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5]

    sol.head = sol.convert_to_node(nums)    
    sol.print_list_node()
