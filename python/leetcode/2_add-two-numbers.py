# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummyHead = ListNode(0)
        ptr = dummyHead

        while(l1 != None or l2 != None) :
            result = 0 + carry

            if(l1 != None) :
                result += l1.val
                l1 = l1.next
             
            if(l2 != None) :
                result += l2.val
                l2 = l2.next

            carry = result // 10

            result = result % 10

            ptr.next = ListNode(result)
            ptr = ptr.next

        if carry > 0:
            ptr.next = ListNode(carry)

        return dummyHead.next

obj = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = obj.addTwoNumbers(l1, l2)

while result:
    print(result.val)
    result = result.next