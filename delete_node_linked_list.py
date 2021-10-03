
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode( node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next

head = [1,2,3,4]
node = 3

output = [1,2,4]