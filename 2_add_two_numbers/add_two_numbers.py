# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sll_to_lst(obj: ListNode):
    result = []
    while obj:
        result.append(obj.val)
        obj = obj.next
    return result


def list_to_sll(lst: list):
    runner = result = ListNode()
    for i in lst:
        runner.next = ListNode()
        runner.next.val = i
        runner = runner.next
    return result.next

###############################################


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = result = ListNode()
        mod = 0
        while l1 or l2 or mod:

            p, q = l1.val if l1 else 0, l2.val if l2 else 0

            mod, head.val = divmod(p + q + mod, 10)

            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
            head.next = ListNode() if l1 or l2 or mod else None
            head = head.next

        return result


if __name__ == '__main__':
    assert Solution().addTwoNumbers(
        list_to_sll([2, 4, 3]),
        list_to_sll([5, 6, 4])
    ) == [7, 0, 8]

    assert Solution().addTwoNumbers(
        list_to_sll([9, 9, 9, 9, 9, 9, 9]),
        list_to_sll([9, 9, 9, 9])
    ) == [8, 9, 9, 9, 0, 0, 0, 1]
