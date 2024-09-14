from typing import *
import math

"""
Remove Node From End of Linked List
You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.
"""
# Definition for singly-linked list.
class ListNode: 
    def __init__(self, val=0, next = None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pass
        

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

input1 = ([1,2,3,4], 2)


head = list_to_linked_list(input1)
# while head != None:
#     print(head.val)
#     head = head.next


sol = res.removeNthFromEnd(head)

# Print Linked list
while sol != None:
    print(sol.val)
    sol = sol.next  # NEXT IS NOT BEING CLEARED IN THE LAST ELEMENT
print("Solution: ", sol)