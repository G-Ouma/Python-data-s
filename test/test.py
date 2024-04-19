'''def write_ints_to_file(output_file_name, input_file_name = ''):
    if input_file_name:
        print("Reading from here")
    else:
        print("Reading from input")


write_ints_to_file('int.txt')'''


'''def two_sum(nums, target):
    num_index_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_index_map:
            return [num_index_map[complement], i]
        num_index_map[num] = i
    return None

# Example usage:
nums = [2, 7, 11, 15]
target = 3
print(two_sum(nums, target))  # Output: [0, 1]'''

'''def greedylist(list):
    maxList = []
    while list:
        no = max(list)
        maxList.append(no)
        list.remove(no)
    return maxList

print(greedylist([2,4,5,6,3,5,33,677,89]))'''

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addNumbers(self, l1:Node, l2: Node):
        # Initialize variables to store the values of the linked list nodes
        x, y, z = 0, 0, 1

        # Traverse the first linked list and accumulate its value in variable x
        while l1:
            x += z * l1.val
            z *= 10
            l1 = l1.next

        # Reset the multiplier for the second linked list
        z = 1
        # Traverse the second linked list and accumulate its value in variable y
        while l2:
            y += z * l2.val
            z *= 10
            l2 = l2.next

        # Calculate the total sum of the two linked lists
        total_sum = x + y
        # Create a dummy head node for the result linked list
        dummyHead = Node(0)
        node = dummyHead

        # Initialize carry for handling sum of digits greater than 9
        carry = 0

        # Iterate until there's no more sum to process and no carry left
        while total_sum > 0 or carry > 0:
            # Calculate the digit to be added to the result linked list
            digit = (total_sum % 10) + carry  # Adding carry to the least significant digit
            # Update carry for the next iteration
            carry = digit // 10
            # Add the digit to the result linked list
            node.next = Node(digit % 10)  # Taking modulus to ensure single digit
            node = node.next
            # Move to the next digit in the sum
            total_sum //= 10

        # Return the next node after the dummy head, which is the start of the result linked list
        return dummyHead.next
    
l1 = Node(2, Node(4, Node(3)))
l2 = Node(5, Node(6, Node(5)))

add_lists = Solution()
sln = add_lists.addNumbers(l1, l2)
results = []
while sln:
    results.append(sln.val)
    sln = sln.next

print(results)