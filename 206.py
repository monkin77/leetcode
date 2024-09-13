from typing import *
import math

"""
Reverse a Linked List
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
"""
# Definition for singly-linked list.
class ListNode: 
    def __init__(self, val=0, next = None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_pointer = head
        prev_pointer = None

        if head is None:
            return None
        
        while True:
            next_elem = curr_pointer.next
            curr_pointer.next = prev_pointer

            if next_elem is None:
                break 

            prev_pointer = curr_pointer # Update the previous pointer
            curr_pointer = next_elem    # Update the new curr pointer

        return curr_pointer



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

input1 = [0,1,2,3]
input2 = []
input3 = [10000,9999,9998,9997,9996,9995,9994,9993,9992,9991,9990]

head = list_to_linked_list(input1)
# while head != None:
#     print(head.val)
#     head = head.next


sol = res.reverseList(head)
print("Solution: ", sol)