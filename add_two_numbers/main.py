# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        runner = result = ListNode()
        mod = 0

        while l1 or l2:

            l1_v = l2_v = 0

            if l1:
                l1_v = l1.val
                l1 = l1.next
            if l2:
                l2_v = l2.val
                l2 = l2.next

            mod, num = divmod(l1_v + l2_v + mod, 10)

            runner.val += num
            if l1 or l2:
                runner.next = ListNode(mod)
            runner = runner.next
            mod = 0
        return result


def sll_to_lst(obj: ListNode):
    result = []
    while obj:
        result.append(obj.val)
        obj = obj.next
    return result


if __name__ == '__main__':
    sol = Solution().addTwoNumbers(
        ListNode(2, ListNode(4)),
        ListNode(5, ListNode(6, ListNode(4)))
    )
    print(sll_to_lst(sol))
