# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummyheader = ListNode(0)
        ptr = dummyheader

        while (list1 != None or list2 != None) :
            if (list1 and list2) :
                if (list1.val <= list2.val) :
                    ptr.next = list1
                    ptr = ptr.next

                    list1 = list1.next
                else :
                    ptr.next = list2
                    ptr = ptr.next

                    list2 = list2.next
            
            else :
                if (list1) :
                    ptr.next = list1
                    ptr = ptr.next
                    list1 = list1.next

                if (list2) :
                    ptr.next = list2
                    ptr = ptr.next
                    list2 = list2.next

        return dummyheader.next


obj = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

result = obj.mergeTwoLists(list1, list2)

while result :
    print(result.val)
    result = result.next