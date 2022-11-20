# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        next1 = list1
        next2 = list2
        result = None
        last = None
        current = None
        while next1 or next2:
                if next1 is not None and next2 is not None:
                    if next1.val < next2.val:
                        last = ListNode(next1.val)
                        next1 = next1.next
                    else:
                        last = ListNode(next2.val)
                        next2 = next2.next

                elif next1 is None:
                    last = next2
                    if result is None:
                        result = last
                    break
                else:
                    last = next1
                    if result is None:
                        result = last
                    break
                
                if current is not None:
                    current.next = last
                if result is None:
                    result = last
                current = last
                    
        return result