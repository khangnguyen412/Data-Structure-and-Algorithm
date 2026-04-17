class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

def main():
    sol = Solution()
    print("result:", sol.deleteDuplicates())  # [1,2]
    # print("result:", sol.deleteDuplicates([1, 1, 2, 3, 3]))  # [1,2,3]


if __name__ == "__main__":
    main()
