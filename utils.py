# ================= Binary Trees ============================= #
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(l: list[int]) -> TreeNode:
    if len(l) == 0:
        return None
    
    queue: list[TreeNode] = []  # Keep nodes that will be filled

    root = TreeNode(val=l[0])
    queue.append(root)
    l.pop(0)

    while len(l) > 0:
        filling_node = queue.pop(0)

        left_node = TreeNode(val = l[0])
        l.pop(0)

        right_node = None
        if len(l) > 0:
            right_node = TreeNode(val = l[0])
            l.pop(0)
        
        filling_node.left = left_node
        queue.append(left_node)
        if right_node:
            filling_node.right = right_node
            queue.append(right_node)
    
    return root

def tree_to_list(root: TreeNode) -> list[TreeNode]:
    if not root:
        return []

    res = []
    queue: list[TreeNode] = []
    queue.append(root)

    while len(queue) > 0:
        curr_node = queue.pop(0)
        res.append(curr_node.val)

        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)

    return res

def print_dfs_tree(root: TreeNode) -> None:
    if not root:
        return
    
    curr_node = root
    queue: list[TreeNode] = []
    queue.append(root)

    while len(queue) > 0:
        curr_node = queue.pop(0)
        print(f"{curr_node.val}-", end="")

        if curr_node.left:
            queue.append(curr_node.left)

        if curr_node.right:
            queue.append(curr_node.right)
        elif curr_node.left:
            # If not right node, but left node
            queue.append(TreeNode(val=None))
    

    





# ================= Linked Lists ============================= #

# Definition for singly-linked list.
class ListNode: 
    def __init__(self, val=0, next = None):
         self.val = val
         self.next = next

class DoublyListNode: 
    def __init__(self, val=0, next = None, prev = None):
         self.val = val
         self.next = next
         self.prev = prev


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

