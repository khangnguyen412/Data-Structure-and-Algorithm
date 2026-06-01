class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def convertToNode(self, arr):
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

    def find_node(self, target=int, head=ListNode):
        cur = head
        while cur:
            if cur.val == target:
                return cur.val
            cur = cur.next


if __name__ == "__main__":
    arr = [1, 2, 3]
    List = ListNode()
    sol = Solution()
    head = sol.convertToNode(arr)
    print(sol.find_node(2, head))
