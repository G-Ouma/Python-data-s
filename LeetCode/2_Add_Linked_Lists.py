# single linked list solution
# two arrays 
# three variables for calculation
# range of node 0 -> 9



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 is not None or l2 is not None:
            # Get the value of each node, or 0 if the node is None
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            
            # Calculate the sum of current digits and carry
            sum = x + y + carry
            
            # Calculate the carry for the next iteration
            carry = sum // 10
            
            # Update the sum if it's greater than 9
            sum %= 10

            # Create a new node with the sum value
            current.next = ListNode(sum)
            current = current.next

            # Move to the next nodes in both linked lists
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        # Handle the final carry if it exists
        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next

# Example usage:
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(5)))
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
while result is not None:
    print(result.val)
    result = result.next
