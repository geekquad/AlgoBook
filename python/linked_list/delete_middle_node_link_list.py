 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr=head
        c=0
        while curr!=None:
            c=c+1
            curr=curr.next
        curr=head
        prev=curr
        if c==1:
            return None
        for i in range(c):
            if i==c//2-1:
                prev=curr
            if i==c//2:
                prev.next=curr.next
                curr=prev
            
            curr=curr.next
        curr=head
        return curr
