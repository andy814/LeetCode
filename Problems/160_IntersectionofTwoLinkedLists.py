from typing import *
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]: # space-efficiency: O(n)
        visited=set({})
        while headA:
            visited.add(headA)
            headA=headA.next
        while headB:
            if headB in visited:
                return headB
            headB=headB.next
        return None

    def getIntersectionNodeDoublePtr(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]: # space-efficiency:O(1)
        initHeadA=headA
        initHeadB=headB
        flagA=False
        flagB=False
        while headA!=headB:
            if headA.next:
                headA=headA.next
            else:
                if not flagA:
                    flagA=True
                    headA=initHeadB
                else:
                    return None
            if headB.next:
                headB=headB.next
            else:
                if not flagB:
                    flagB=True
                    headB=initHeadA
                else:
                    return None
        return headA
