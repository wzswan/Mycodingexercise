# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 12:23:38 2016

@author: wzswan
"""

#class ListNode:
#   def __init__(self,x):
#        self.val = x
#        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        dummy = cur = ListNode(-1)
        carry = 0
        
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            
            sum = a + b + carry
            cur.next = ListNode(sum % 10)
            cur = cur.next
            carry = sum / 10
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry > 0:
            cur.next = ListNode(1)
        
        return dummy.next
    