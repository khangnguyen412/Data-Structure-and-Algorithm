class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"
    
    def __str__(self):
        return str(self.val)


class Solution:
    def convertToListNode(self, arr=None):
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

    def printListNode(self, head: ListNode):
        cur = head
        while cur:
            next_val = cur.next.val if cur.next else None
            print(f"Value: {cur.val} | Next: {next_val}")
            cur = cur.next


def main():
    sol = Solution()
    nums = [1, 2, 3, 4, 5]

    head = sol.convertToListNode(nums)
    sol.printListNode(head)


if __name__ == "__main__":
    main()
