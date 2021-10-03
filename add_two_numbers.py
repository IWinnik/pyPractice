# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    l1.reverse()
    l2.reverse()
    l1s = [str(i) for i in l1]
    l1s = "".join(l1s)
    n1 = int(l1s)
    l2s = [str(i) for i in l2]
    l2s = "".join(l2s)
    n2 = int(l2s)
    res_num = n1 + n2

    res_str = str(res_num)
    res_list = list(res_str)
    res_list.reverse()
    res_list = [int(i) for i in res_list]
    return res_list

res = addTwoNumbers([2,4,3],[5,6,4])
print(res)