from typing import *
import math

"""
Reorder Linked List
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
"""
# Definition for singly-linked list.
class ListNode: 
    def __init__(self, val=0, next = None, prev = None):
         self.val = val
         self.next = next
         self.prev = prev

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Let's create the link to the prev element of the linked list
        # -- Doubly-Linked List
        curr_pt = head
        prev_pt = None
        while curr_pt:
            curr_pt.prev = prev_pt
            prev_pt = curr_pt
            curr_pt = curr_pt.next
            
        # Set the left and right pointers on the Linked List
        right_pt = prev_pt
        left_pt = head

        # So for each element in the original linked list, we will insert an element in the middle of 2 starting from the end
        # Therefore, we will only do this for len // 2
        while left_pt and (left_pt != right_pt) and left_pt.val <= right_pt.val:
            # Set the next pointer of the right element to the node the left ptr was connected to
            right_pt.next = left_pt.next
            # Set the next point of the left node to the right_ptr
            left_pt.next = right_pt

            # Move the right_pt to the left
            right_pt = right_pt.prev
            # Move the left ptr to the right (2 times)
            for i in range(2):
                left_pt = left_pt.next

        if right_pt.next == right_pt.next:
            right_pt.next = None
        # right_pt.next = None

        return # head
        

def list_to_linked_list(l) -> ListNode:

    if len(l) == 0:
        return None
    
    prevNode = None
    head = None
    for i in range(len(l)):
        currNode = ListNode(l[i], None)
        if head == None:
            head = currNode
            # Save the head of the list

        if prevNode:
            # Add the next node to the previous node
            prevNode.next = currNode
        
        prevNode = currNode

    return head


res = Solution()

input1 = [2,4,6,8]
input2 = [2,4,6,8,10]
input3 = []

head = list_to_linked_list(input2)
# while head != None:
#     print(head.val)
#     head = head.next


res.reorderList(head)
sol = head

# Print Linked list
while sol != None:
    print(sol.val)
    sol = sol.next  # NEXT IS NOT BEING CLEARED IN THE LAST ELEMENT
print("Solution: ", sol)