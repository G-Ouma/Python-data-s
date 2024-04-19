class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addNumbers(self, l1: ListNode, l2: ListNode):
        # variable initialization to store linkedlist nodes
        x, y, z = 0, 0, 1

        # Traverse the first linked list and accumulate its value in variable x
        while l1:
            x += z*l1.val
            z *= 10
            l1 = l1.next

        z = 1
        while l2:
            y += z*l2.val
            z *= 10
            l2 = l2.next

        sum = x + y
        dummyHead = ListNode(0)
        node = dummyHead

        carry = 0

        while sum > 0 or carry > 0:
            digit = (sum % 10) + carry
            carry = digit // 10
            node.next = ListNode(digit % 10)
            node = node.next
            sum = sum // 10

        return dummyHead.next

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(5)))

add_lists = Solution()
sln = add_lists.addNumbers(l1, l2)
results = []
while sln:
    results.append(sln.val)
    sln = sln.next

print(results)
