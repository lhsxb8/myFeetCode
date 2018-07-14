# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = b = 0
        i_1 = i_2 = 1
        while l1 != None:
            a += i_1 * l1.val
            l1 = l1.next
            i_1 = i_1 * 10

        while l2 != None:
            b += i_2 * l2.val
            l2 = l2.next
            i_2 = i_2 * 10

        ans = a + b
        head = ListNode(0)
        p = ListNode(0)
        p = head

        #P 为移动指针
        while(ans >= 10 ):
            temp = ListNode(None)
            p.val = ans % 10
            p.next = temp
            p = temp
            ans = ans//10
        
        p.val = ans % 10

        return head

        